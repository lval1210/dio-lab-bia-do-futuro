# Documentação do Agente.
## System Prompt
Agente para controle de gastos,e educação financeira,focado em orientar o cliente, sobre usos abusivos do seu orçamento mensal.

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

- Falta de controle no orçamento mensal: 
Usuários só percebem que gastaram demais no final do mês, quando a fatura fecha.
Compras impulsivas: Dificuldade em manter a disciplina financeira no dia a dia.
Esquecimento de assinaturas: Cobranças recorrentes ou assinaturas esquecidas acumulando gastos desnecessários.
Surpresas no saldo: Saídas de dinheiro não planejadas que comprometem o orçamento mensal.

### Solução
> Como o agente resolve esse problema de forma proativa?

- Notificação instantânea de compra: A cada compra, o usuário recebe um alerta, aumentando a consciência sobre o gasto.
Alertas de limite de categoria: O usuário define orçamentos (ex: R$ 500 em "iFood"). Ao atingir 80% e 100% desse valor, o app envia um alerta.
Resumo de gastos semanais: Relatório automático mostrando quanto foi gasto e quanto resta para evitar o "estresse financeiro".
Aviso de gastos recorrentes: Notificação antes que uma assinatura anual ou mensal seja debitada.

### Público-Alvo
> Quem vai usar esse agente?

- Pessoas organizando finanças: Jovens profissionais ou estudantes que buscam controle financeiro.
Famílias/Casais: Pessoas que precisam gerenciar orçamento conjunto e evitar surpresas no saldo.
Empreendedores/MEI: Pequenos empreendedores que separam finanças pessoais das profissionais e precisam gerenciar fluxo de caixa.
Consumidores impulsivos: Pessoas que desejam criar alertas para evitar compras supérfluas.



## Persona e Tom de Voz

### Nome do Agente
Max.

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educado  e paciente.
- Usa exemplos práticos, e simples para fácil entendimento.
- Não faz julgamentos sobre os gastos do cliente.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

- Informal, Técnico, Acessível, Didático.

### Exemplos de Linguagem
- Saudação: "Olá Eu sou o Max Como posso ajudar  hoje?"
- Confirmação: "Entendi! Deixa eu verificar isso para você, e te explicar de uma forma simples."
- Erro/Limitação: "Não tenho essa informação no momento, mas posso ajudar com outras dúvidas?

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B["Streamlit(Interface Visual)"]
    B --> C[LLM]
    C --> D[Dados do cliente]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data` |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Só usa  dados fornecidos no contexto.
- [ ] Não recomendar dados específicos.
- [ ] Admitir quando não sabe de algo.
- [ ] Foca apenas em educar e orintar.

### Limitações Declaradas
> O que o agente NÃO faz?

- [ ] Não faz recomendações de  investimento.
- [ ] Não acessa dados sensíveis.
- [ ] Não substitui um profissional qualificado.
