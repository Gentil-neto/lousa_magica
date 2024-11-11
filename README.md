# Lousa mágica - Projeto de Visão computacional  

Lousa Mágica com Visão Computacional
Este projeto implementa uma lousa virtual interativa usando visão computacional, onde o usuário pode desenhar no ar utilizando apenas o movimento do dedo indicador. A detecção de mãos e o desenho em tempo real são realizados com as bibliotecas 

## Tecnologias Utilizadas

[<img src="https://github.com/tandpfun/skill-icons/raw/main/icons/Python-Dark.svg" width="40" height="40" />](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)

OpenCV e MediaPipe em Python.

Funcionalidades
Detecção de mão e rastreamento da posição do dedo indicador.
Desenho contínuo na "lousa mágica" com o movimento do dedo.
Limpeza automática da lousa após 5 segundos sem movimento.
Interação sem toque, simulando uma experiência de desenho intuitiva e segura.

Tecnologias Utilizadas
Python: Linguagem de programação principal.
OpenCV: Para captura de vídeo e processamento de imagem.
MediaPipe: Para detecção e rastreamento de mãos e dedos.
NumPy: Para manipulação de arrays e criação da tela virtual de desenho.

Instalação
1 - Clone o repositório

2 - instale as dependencias 
  pip install opencv-python mediapipe numpy

3 - python lousa_magica.py

Como Funciona
A câmera é ativada e detecta a mão do usuário em tempo real.
Quando o dedo indicador é levantado, o sistema ativa o modo de desenho.
Movendo o dedo, o sistema traça uma linha na tela simulando uma lousa mágica.
Após 5 segundos sem movimento, a lousa é limpa automaticamente.
Exemplos de Aplicação
Educação: Ferramenta interativa para aulas ou apresentações.
Saúde: Interface sem toque para ambientes estéreis.
Entretenimento: Jogos e atividades de desenho para crianças.
Contato
Para dúvidas ou sugestões, entre em contato:

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Gentil.araujo@outlook.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gentiln)



