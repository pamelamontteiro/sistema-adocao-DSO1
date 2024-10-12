# Projeto de um Sistema de Adoção de Gatos e Cachorros - ONS

 Este projeto foi desenvolvido durante as aulas de Desenvolvimento de Sistemas Orientados a Objetos I (UFSC). 

O objetivo do sistema é facilitar o processo de adoção de gatos e cachorros.

Realizado em parceria por Pamela Monteiro e Thabata.
Implementação em Python. 🐍
    


<img height="200" src="gatos.gif">

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

- <p><strong> Relatórios </strong>
       
    *   Relatório de Adoções
    *   Relatório de Doações
    *   Listagem de Animais Disponíveis para Adoção

## DIAGRAMA UML


#Diagrama de Classe (UML) - 
###
```mermaid
classDiagram
    class Animal{
        - Numero_chip : int
        - nome: str
        - raca: str
        - castrado=bool
      + < create>> __init__(numero_chip, nome, raca, castrado)
      +add_vacina(vacina: Historico_vacinacao)
    }
   class Vacina {
        - nome_vacina: str
        - codigo_vacina: int
        + < create>> __init__(nome_vacina,codigo_vacina)
      }
    class Historico_vacinacao {
      - data_de_vacinacao: date
      - vacina: Vacina
      + < create>> __init__(data_de_vacinacao, vacina)
    }

    class Cachorro {
       - tamanho: str
       + < create>> __init__(numero_chip, nome, raca, castrado,tamanho)
    }
     class Gato {
      + < create>> __init__(numero_chip, nome, raca, castrado)
    }
    class Pessoa{
      - nome: str
      - cpf: str
      - data_nascimento: date
      -  endereco: str
      + << create >> __init__(nome,cpf,data_nascimento,endereco)
    }

    class Adotante{
        - tipo_habitacao: str
        - tem_outros_animais: bool
      + << create >> __init__(nome,cpf,data_nascimento, endereco, tipo_habitacao, tem_outros_animais)
    }

       class Doador{
      + << create >> __init__(nome,cpf,data_nascimento,endereco)
    }

        class Doacao{
        - data_de_doacao: date
        - motivo: str
      + << create >> __init__(animal, doador,data_de_doacao,motivo)
    }
     class Adoacao{
        -  data_adocao: date
        -  termo_assinado: bool
      + << create >> __init__(animal, adotante,data_adocao,termo_assinado)
    }

      class Registro{
      + listar_animais_disponivel()
      + Adoacao(data_adocao,animal,adotante,termo_assinado)
      + Doacao(data_de_docao,animal, doador, motivo)
    }
  


    Animal <|-- Gato
    Animal <|-- Cachorro
    Animal "1" <-- "n" Historico_vacinacao
    Pessoa <|-- Doador
    Pessoa <|-- Adotante
    Vacina <|-- Historico_vacinacao 
    Doacao "n" --> "1" Doador
    Adotante "-" <-- "1" Adoacao
    Animal "0 .. *" <-- "1" Registro
    Registro *-- Adoacao
    Registro *-- Doacao
```

## Diagrama MVC 
###
```mermaid
classDiagram
    namespace Model {
        class Animal{
        - Numero_chip : int
        - nome: str
        - raca: str
        - castrado=bool
      + < create>> __init__(numero_chip, nome, raca, castrado)
      +add_vacina(vacina: Historico_vacinacao)
    }
   class Vacina {
        - nome_vacina: str
        - codigo_vacina: int
        + < create>> __init__(nome_vacina,codigo_vacina)
      }
    class Historico_vacinacao {
      - data_de_vacinacao: date
      - vacina: Vacina
      + < create>> __init__(data_de_vacinacao, vacina)
    }

    class Cachorro {
       - tamanho: str
       + < create>> __init__(numero_chip, nome, raca, castrado,tamanho)
    }
     class Gato {
      + < create>> __init__(numero_chip, nome, raca, castrado)
    }
    class Pessoa{
      - nome: str
      - cpf: str
      - data_nascimento: date
      -  endereco: str
      + << create >> __init__(nome,cpf,data_nascimento,endereco)
    }

    class Adotante{
        - tipo_habitacao: str
        - tem_outros_animais: bool
      + << create >> __init__(nome,cpf,data_nascimento, endereco, tipo_habitacao, tem_outros_animais)
    }

       class Doador{
      + << create >> __init__(nome,cpf,data_nascimento,endereco)
    }

        class Doacao{
        - data_de_doacao: date
        - motivo: str
      + << create >> __init__(animal, doador,data_de_doacao,motivo)
    }
     class Adoacao{
        -  data_adocao: date
        -  termo_assinado: bool
      + << create >> __init__(animal, adotante,data_adocao,termo_assinado)
    }

      class Registro{
      + listar_animais_disponivel()
      + Adoacao(data_adocao,animal,adotante,termo_assinado)
      + Doacao(data_de_docao,animal, doador, motivo)
    }
    }

    namespace Controller {
        class ControladorGato {
            - gatos: List[Gato]
            + <<create>> __init__()
            + incluir_gato(numero_chip, nome, raca, castrado)
            + alterar_gato(numero_chip)
            + excluir_gato(numero_chip)
            + listar_gatos()
            + retonar()
            + abrir_tela_gato()
        }
    }

    namespace View {
        class TelaGato {
            - acoes_da_tela
            - nome_gato
            - raca_gato
            - numero_do_chip_gato
            - historico_vacinacao
            - castrado
            + <<create>> __init__()
            + opcoes_acoes()
            + cadastrar_gato()
            + listar_gatos()
        }
    }
    
  


    Animal <|-- Gato
    Animal <|-- Cachorro
    Animal "1" <-- "n" Historico_vacinacao
    Pessoa <|-- Doador
    Pessoa <|-- Adotante
    Vacina <|-- Historico_vacinacao 
    Doacao "n" --> "1" Doador
    Adotante "-" <-- "1" Adoacao
    Animal "0 .. " <-- "1" Registro
    Registro-- Adoacao
    Registro *-- Doacao
    ControladorGato --> Gato
    TelaGato <--> ControladorGato
```


