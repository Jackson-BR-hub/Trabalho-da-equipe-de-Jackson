class CadastroFuncionarios:
    def __init__(self):
        self.funcionarios = {}

    def adicionar_funcionario(self, id_funcionario, nome, cargo, salario):
        if id_funcionario in self.funcionarios:
            print(f"Já existe um funcionário com o ID {id_funcionario}.")
        else:
            self.funcionarios[id_funcionario] = {
                'nome': nome,
                'cargo': cargo,
                'salario': salario
            }
            print(f"Funcionário adicionado com sucesso! ID: {id_funcionario}")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Não há funcionários cadastrados.")
        else:
            print("\nLista de Funcionários:")
            for id_funcionario, info in self.funcionarios.items():
                print(f"ID: {id_funcionario}, Nome: {info['nome']}, Cargo: {info['cargo']}, Salário: R${info['salario']:.2f}")
            print()

    def buscar_funcionario_por_id(self, id_funcionario):
        if id_funcionario in self.funcionarios:
            info = self.funcionarios[id_funcionario]
            print(f"Detalhes do funcionário ID {id_funcionario}:")
            print(f"Nome: {info['nome']}")
            print(f"Cargo: {info['cargo']}")
            print(f"Salário: R${info['salario']:.2f}")
        else:
            print(f"Funcionário com ID {id_funcionario} não encontrado.")

# Função principal para testar o programa
def main():
    cadastro = CadastroFuncionarios()

    # Exemplo de adicionar funcionários
    cadastro.adicionar_funcionario(1001, "João", "Analista de Sistemas", 4500.00)
    cadastro.adicionar_funcionario(1002, "Maria", "Gerente de Projetos", 6000.00)

    # Exemplo de listar funcionários
    cadastro.listar_funcionarios()

    # Exemplo de buscar funcionário por ID
    cadastro.buscar_funcionario_por_id(1001)
    cadastro.buscar_funcionario_por_id(1003)  # Testando ID inexistente

if __name__ == "__main__":
    main()