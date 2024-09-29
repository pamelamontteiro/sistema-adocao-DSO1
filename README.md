# Projeto de um Sistema de Adoção de Gatos e Cachorros - ONS

 <img align="left" height="200" src="gatos.gif">
 
     Este projeto foi desenvolvido durante as aulas de Desenvolvimento de Sistemas Orientados a Objetos I (DSO) na Universidade Federal de Santa Catarina (UFSC). O objetivo do sistema é facilitar o processo de adoção de gatos e cachorros.

    Realizado em parceria por Pamela Monteiro e Thabata.
    Implementação em Python. 🐍
    
<br>
<br>

## Entidades

Objetivo: Garantir a adoção responsável de animais.

- <p><strong> Cadastro de Animais </strong>

    *   Número do chip
    *   Nome
    *   Raça
    *   Tamanho (para cães): Pequeno, Médio, Grande

- <p><strong> Histórico de Vacinação </strong>

    *   Data
    *   Vacina aplicada
    *   Cadastro de Doador

- <p><strong> Registro de Doação </strong>

    *   Data da doação
    *   Animal doado
    *   Doador
    *   Motivo da doação
    *   Cadastro de Adoção

- <p><strong> Adotante </strong>

    *   CPF
    *   Nome
    *   Data de nascimento
    *   Endereço
    *   Tipo de habitação (Casa ou Apartamento)
    *   Possui outros animais (Sim ou Não)

- <p><strong> Processo de Adoção </strong>

    *   Avaliação do perfil
    *   Escolha do animal
    *   Assinatura do termo de responsabilidade

- <p><strong> Registro de Adoção </strong>

    *   Data
    *   Animal adotado
    *   Adotante
    *   Termo de responsabilidade assinado (Sim ou Não)

    <img align="right" height="100" src="gato-cao-amigos.gif">

- <p><strong> Relatórios </strong>
       
    *   Relatório de Adoções
    *   Relatório de Doações
    *   Listagem de Animais Disponíveis para Adoção

## DIAGRAMA UML


<img src="DIAGRAMA.jpeg">


## Relacionamentos

*   Animal tem um HistoricoVacina (1 para N)
*   Doador está relacionado a Doacao (1 para N)
*   Animal está relacionado a Doacao (1 para 1)
*   Adotante está relacionado a Adoção (1 para N)
*   Animal está relacionado a Adoção (1 para 1)



