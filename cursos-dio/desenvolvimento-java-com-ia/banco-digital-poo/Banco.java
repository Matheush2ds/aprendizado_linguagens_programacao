import java.util.ArrayList;
import java.util.List;

public class Banco {
    private List<Conta> contas;

    public Banco(String nome) {
        this.contas = new ArrayList<>();
    }

    public void adicionarConta(Conta conta) {
        contas.add(conta);
    }

    public void listarContas() {
        for (Conta conta : contas) {
            System.out.println(String.format("Agencia: %d, Numero: %d, Cliente: %s", 
                                              conta.getAgencia(), conta.getNumero(), conta.cliente.getNome()));
        }
    }
}
