public class ContaPoupanca extends Conta {
    private double taxaJuros;

    public ContaPoupanca(Cliente cliente, double taxaJuros) {
        super(cliente);
        this.taxaJuros = taxaJuros;
    }

    public void aplicarJuros() {
        saldo += saldo * (taxaJuros / 100);
    }

    @Override
    public void imprimirExtrato() {
        System.out.println("=== Extrato Conta Poupança ===");
        super.imprimirExtrato();
    }
}
