public class Main {
    public static void main(String[] args) {
        Banco banco = new Banco("Banco Digital");

        Cliente cliente1 = new Cliente("Alice", "12345678900");
        Cliente cliente2 = new Cliente("Bruno", "98765432100");

        Conta cc = new ContaCorrente(cliente1);
        Conta cp = new ContaPoupanca(cliente2, 0.5);

        banco.adicionarConta(cc);
        banco.adicionarConta(cp);

        cc.depositar(500);
        cc.sacar(200);
        cc.transferir(100, cp);

        cp.depositar(300);
        ((ContaPoupanca) cp).aplicarJuros();

        System.out.println("=== Lista de Contas ===");
        banco.listarContas();

        System.out.println("\nExtrato da Conta Corrente:");
        cc.imprimirExtrato();

        System.out.println("\nExtrato da Conta Poupança:");
        cp.imprimirExtrato();
    }
}
