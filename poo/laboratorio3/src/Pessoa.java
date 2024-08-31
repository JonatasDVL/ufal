public class Pessoa {
  private String nome;
  private String telefone;
  private String email;
  private String senha;

  public Pessoa(String nome, String telefone, String email, String senha){
    this.nome = nome; 
    this.telefone = telefone;
    this.email = email;
    this.senha = senha;
  }

  public String getNome(){
    return this.nome;
  };

  public String getTelefone(){
    return this.telefone;
  };

  public String getEmail(){
    return this.email;
  };

  public boolean validaSenha(String senha){
    boolean valido = false;
    if (this.senha != null && this.senha.equals(senha)){
      valido = true;
    }
    return valido;
  };

  @Override
  public boolean equals(Object obj) {
    boolean retorno = false;
    if (obj instanceof Pessoa && ((Pessoa)obj).getEmail().equals(this.email)){
        retorno = true;
    };
    return retorno;
  };

  @Override
  public String toString(){
    return this.nome + " - " + this.telefone + " - " + this.email;
  }; 
}
