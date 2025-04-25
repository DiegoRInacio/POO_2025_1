package zz_Prova.Java;

public class CadastroPessoa {
    // Atributos públicos
    public String nome;
    public String cpf;
    public String profissao;
    public String endereco;

    // Construtor para inicializar tudo certinho
    public CadastroPessoa(String nome, String cpf, String profissao, String endereco) {
        this.nome = nome;
        this.cpf = cpf;
        this.profissao = profissao;
        this.endereco = endereco;
    }

    // Método para apresentar a pessoa de um jeito educado
    public void apresentar() {
        System.out.println("Nome: " + nome);
        System.out.println("CPF: " + cpf);
        System.out.println("Profissão: " + profissao);
        System.out.println("Endereço: " + endereco);
    }

    // Um mini teste para ver funcionando
    public static void main(String[] args) {
        CadastroPessoa pessoa = new CadastroPessoa(
            "Lucas Oliveira",
            "123.456.789-00",
            "Engenheiro de Software",
            "Rua das Palmeiras, 100 - Centro"
        );

        pessoa.apresentar(); // Bora ver quem é essa pessoa
    }
}