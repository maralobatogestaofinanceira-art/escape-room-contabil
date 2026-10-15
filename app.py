import streamlit as st

# Configuração da página
st.set_page_config(page_title="Escape Room: Escrituração", page_icon="🔐", layout="centered")

# --- CONTROLE DE ACESSO ---
alunos_permitidos = ["Selecione...", "Basica 1"]

st.title("🔐 Escape Room Contábil")
st.markdown("Bem-vindos à monitoria de **Contabilidade Básica I**. Sigam o ciclo contabilístico completo: do Diário (Eventos 1 a 12), passando pelos Razonetes, até fechar o Balanço Patrimonial!")

# Inicializa as variáveis de controle (começa na Fase 1)
if 'fase' not in st.session_state:
    st.session_state.fase = 1

usuario = st.selectbox("Identifique-se para aceder:", alunos_permitidos)

if usuario != "Selecione...":
    st.success(f"Acesso liberado para: {usuario}")
    
    # Barra de progresso (15 fases totais = 12 Eventos + Razão + DRE + Balanço)
    progresso = (st.session_state.fase - 1) / 15
    st.progress(min(progresso, 1.0))
    st.write(f"**Progresso:** Sala {min(st.session_state.fase, 15)} de 15")
    st.markdown("---")

    # Base de dados com todas as fases e respostas (baseado no ficheiro Excel)
    fases_data = [
        {
            "titulo": "📖 Evento 1: Abertura da Empresa",
            "info": "**Fato:** Subscrição de Capital de R$ 100.000,00, integralizando R$ 60.000,00 no ato via conta bancária.",
            "pergunta": "Qual o valor do saldo restante debitado na conta 'Capital a Integralizar'?",
            "resposta": 40000,
            "erro": "Capital Subscrito menos o que já foi para o banco."
        },
        {
            "titulo": "📖 Evento 2: A Primeira Compra",
            "info": "**Fato:** Aquisição de mercadorias a prazo (XYZ Comércio Ltda.) por R$ 6.000,00.",
            "pergunta": "Qual o valor a ser CREDITADO na conta 'Fornecedores'?",
            "resposta": 6000,
            "erro": "Na compra a prazo, a obrigação com o fornecedor assume o valor total."
        },
        {
            "titulo": "📖 Evento 3: A Primeira Venda",
            "info": "**Fato:** Venda de 50% do estoque a prazo por R$ 5.000,00.",
            "pergunta": "Sabendo que tínhamos R$ 6.000 em estoque, qual o valor do Custo da Mercadoria Vendida (CMV)?",
            "resposta": 3000,
            "erro": "Calcule 50% do saldo de estoque disponível."
        },
        {
            "titulo": "📖 Evento 4: Repondo o Estoque",
            "info": "**Fato:** Aquisição de mercadorias à vista (banco) por R$ 20.000,00.",
            "pergunta": "Qual o valor exato DEBITADO na conta 'Mercadorias'?",
            "resposta": 20000,
            "erro": "É o valor da mercadoria que entra no ativo."
        },
        {
            "titulo": "📖 Evento 5: A Segunda Venda",
            "info": "**Fato:** Venda de 50% do saldo de estoque à vista (caixa) por R$ 18.000,00.",
            "pergunta": "Qual o valor do novo CMV? (Dica: sobrou 3.000 do Evento 3 e comprou mais 20.000 no Evento 4. Calcule 50% do total)",
            "resposta": 11500,
            "erro": "Some os R$ 3.000 restantes com os novos R$ 20.000. Depois aplique os 50%."
        },
        {
            "titulo": "📖 Evento 6: Venda Mista",
            "info": "**Fato:** Venda de 50% do estoque (sendo 50% à vista banco e 50% a prazo) por R$ 5.000,00.",
            "pergunta": "Qual o valor DEBITADO na conta 'Clientes' (referente apenas à parte a prazo)?",
            "resposta": 2500,
            "erro": "Apenas metade da venda de 5.000 foi a prazo."
        },
        {
            "titulo": "📖 Evento 7: Compra Mista",
            "info": "**Fato:** Compra de mercadorias por R$ 10.000,00 (50% à vista no caixa e 50% a prazo).",
            "pergunta": "Qual o valor CREDITADO na conta 'Caixa' pela saída do dinheiro?",
            "resposta": 5000,
            "erro": "Metade do valor do fornecimento saiu do caixa."
        },
        {
            "titulo": "📖 Evento 8: Pagamento",
            "info": "**Fato:** Pagamento de R$ 2.000,00 ao fornecedor XYZ em dinheiro (caixa).",
            "pergunta": "Qual o valor DEBITADO na conta 'Fornecedores' reduzindo a vossa dívida?",
            "resposta": 2000,
            "erro": "O valor debitado no passivo é igual ao valor pago."
        },
        {
            "titulo": "📖 Evento 9: Móveis e Utensílios",
            "info": "**Fato:** Aquisição de móveis por R$ 3.000,00 à vista (banco).",
            "pergunta": "Qual o valor CREDITADO na conta 'Bancos Conta Movimento'?",
            "resposta": 3000,
            "erro": "A saída do banco corresponde ao valor total pago pelos móveis."
        },
        {
            "titulo": "📖 Evento 10: O Veículo",
            "info": "**Fato:** Aquisição de um veículo a prazo em 90 dias (Considere o valor da nota: R$ 40.000,00).",
            "pergunta": "Qual o valor DEBITADO na conta 'Veículos'?",
            "resposta": 40000,
            "erro": "Utilize o valor exato informado para o veículo."
        },
        {
            "titulo": "📖 Evento 11: O Imóvel",
            "info": "**Fato:** Compra de imóvel de R$ 100.000,00 a prazo (Terreno avaliado em 30.000 e Edificações em 70.000).",
            "pergunta": "No Diário, separamos os bens. Qual o valor DEBITADO especificamente na conta 'Edificações'?",
            "resposta": 70000,
            "erro": "Use a segregação dada no enunciado (não coloque o valor do terreno)."
        },
        {
            "titulo": "📖 Evento 12: Integralização Final",
            "info": "**Fato:** Sócios integralizam 40% do que ainda deviam no Evento 1, com depósito no banco.",
            "pergunta": "Lembrando que no Evento 1 a dívida era de R$ 40.000,00, qual o valor que entra a DÉBITO no 'Banco' agora?",
            "resposta": 16000,
            "erro": "Calcule 40% de 40.000."
        },
        {
            "titulo": "⚖️ Sala 13: Os Razonetes (Balancete)",
            "info": "**Fato:** Todos os registos do Diário concluídos. É hora de verificar os saldos dos razonetes.",
            "pergunta": "Verifiquem o razonete do CAIXA. Entrada: 18.000 (Ev 5). Saídas: 5.000 (Ev 7) e 2.000 (Ev 8). Qual o saldo devedor final da conta Caixa?",
            "resposta": 11000,
            "erro": "Entradas menos as saídas de dinheiro."
        },
        {
            "titulo": "📈 Sala 14: Demonstração do Resultado (DRE)",
            "info": "**Fato:** Apuração do Resultado. As Receitas de Vendas somam R$ 28.000 e o CMV totaliza R$ 20.250.",
            "pergunta": "Qual o valor do Resultado do Exercício (Lucro) a ser transferido para o PL?",
            "resposta": 7750,
            "erro": "Basta fazer: 28.000 menos 20.250."
        },
        {
            "titulo": "🏛️ Sala 15: Balanço Patrimonial",
            "info": "**Fato:** O grande momento! O Lucro foi para o PL. Agora verifiquem a equação fundamental: Ativo = Passivo + PL.",
            "pergunta": "Qual é o valor exato do TOTAL DO ATIVO?",
            "resposta": 232750,
            "erro": "Corresponde ao total do vosso Balanço no Excel. Ativo Circulante + Ativo Não Circulante."
        }
    ]

    indice = st.session_state.fase - 1
    
    # Motor do Jogo
    if indice < len(fases_data):
        fase_atual = fases_data[indice]
        st.header(fase_atual["titulo"])
        st.info(fase_atual["info"])
        
        # O key usa o índice para não haver conflitos entre as perguntas
        resp = st.number_input(fase_atual["pergunta"], min_value=0, step=1000, key=f"input_{indice}")
        
        if st.button("Validar e Avançar 🚀"):
            if resp == fase_atual["resposta"]:
                st.session_state.fase += 1
                st.rerun() # Atualiza a tela imediatamente para a próxima fase
            else:
                st.error("Incorreto! Dica: " + fase_atual["erro"])
    else:
        st.balloons()
        st.success("🎉 PARABÉNS! A vossa equipa escapou do labirinto e o Balanço Patrimonial fechou na perfeição! O Professor Erminio está orgulhoso!")
else:
    st.warning("Por favor, selecione a vossa equipa para iniciar o jogo.")
