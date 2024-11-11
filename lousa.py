#pip install mediapipe instalação do pacote

import cv2
import mediapipe as mp
import numpy as np
import time

# Inicialização da câmera
cap = cv2.VideoCapture(0)

# Inicialização do MediaPipe para a detecção de mãos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Criação da janela
cv2.namedWindow('Lousa Mágica')

# Variáveis para armazenar pontos de desenho e estado
draw = False
board = np.zeros((480, 640, 3), dtype=np.uint8)
last_draw_time = time.time()
prev_x, prev_y = None, None

def is_index_finger_up(hand_landmarks):
    finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
    return finger_tip.y < finger_pip.y

while True:
    # Captura o frame da câmera
    ret, frame = cap.read()
    if not ret:
        break

    # Espelha o frame para um melhor controle
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa a imagem para detectar as mãos
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if is_index_finger_up(hand_landmarks):
                draw = True
                last_draw_time = time.time()
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, _ = frame.shape
                cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                if prev_x is not None and prev_y is not None:
                    cv2.line(board, (prev_x, prev_y), (cx, cy), (255, 255, 255), 5)
                prev_x, prev_y = cx, cy
            else:
                draw = False
                prev_x, prev_y = None, None

            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        draw = False
        prev_x, prev_y = None, None

    # Limpar a tela se a mão estiver abaixada por 5 segundos
    if time.time() - last_draw_time > 5:
        board = np.zeros((480, 640, 3), dtype=np.uint8)

    # Combinar o board e a imagem da câmera
    combined = cv2.addWeighted(frame, 0.5, board, 0.5, 0)
    cv2.imshow('Lousa Mágica', combined)

    # Tecla 'q' para sair
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Liberação da câmera e destruição das janelas
cap.release()
cv2.destroyAllWindows()
hands.close()