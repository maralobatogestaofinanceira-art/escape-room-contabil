import streamlit as st

# Configuração da página
st.set_page_config(page_title="Escape Room: O Mistério do Balanço", page_icon="🔐")

# --- CONTROLE DE ACESSO ---
# Você pode adicionar ou remover nomes aqui. Se um aluno sair, basta tirar o nome dele.
alunos_permitidos = ["Selecione...", "Equipe 1", "Equipe 2", "Equipe 3", "João Silva", "Maria Souza"]

st.title("🔐 Escape Room Contábil")
st.markdown("Bem-vindo! Resolva os lançamentos do Exercício 4 para destravar os cadeados e fechar o Balanço.")

# Variáveis de controle de fase
if 'fase' not in st.session_state:
    st.session_state.fase = 0

usuario = st.selectbox("Identifique-se para acessar:", alunos_permitidos)

if usuario != "Selecione...":
    st.success(f"Acesso liberado para: {usuario}")
    
    # FASE 1
    if st.session_state.fase >= 0:
        st.header("🚪 Sala 1: A Abertura da Empresa")
        st.info("**Fato 1:** Subscrição de Capital de R$ 100.000, com integralização de R$ 60.000 no banco.")
        resp1 = st.number_input("Qual o saldo restante da conta 'Capital a Integralizar'? (Digite apenas o número)", min_value=0, step=1000, key="r1")
        
        if st.button("Destravar Sala 1"):
            if resp1 == 40000:
                st.session_state.fase = max(st.session_state.fase, 1)
                st.success("Cadeado aberto! O saldo é R$ 40.000,00.")
            else:
                st.error("Senha incorreta. Revise o razonete de Capital a Integralizar.")

    # FASE 2
    if st.session_state.fase >= 1:
        st.markdown("---")
        st.header("📦 Sala 2: O Desafio do Estoque")
        st.info("**Fatos 2 e 3:** Após comprar R$ 6.000 em mercadorias, a empresa vende 50% do estoque a prazo por R$ 5.000.")
        resp2 = st.number_input("Qual o valor do Custo da Mercadoria Vendida (CMV) a ser contabilizado no Fato 3?", min_value=0, step=1000, key="r2")
        
        if st.button("Destravar Sala 2"):
            if resp2 == 3000:
                st.session_state.fase = max(st.session_state.fase, 2)
                st.success("Cadeado aberto! 50% de R$ 6.000,00 = R$ 3.000,00.")
            else:
                st.error("Senha incorreta. Lembre-se que o CMV é baseado no custo de aquisição, não no preço de venda.")

    # FASE 3
    if st.session_state.fase >= 2:
        st.markdown("---")
        st.header("🏢 Sala 3: Imobilizando Recursos")
        st.info("**Fato 11:** Aquisição de imóvel por R$ 100.000 (Terreno: 30.000 / Edificação: 70.000) a prazo.")
        resp3 = st.number_input("Qual o valor exato a ser debitado APENAS na conta 'Edificações'?", min_value=0, step=1000, key="r3")
        
        if st.button("Destravar Sala 3"):
            if resp3 == 70000:
                st.session_state.fase = max(st.session_state.fase, 3)
                st.success("Cadeado aberto! Terrenos e Edificações são contabilizados separadamente.")
            else:
                st.error("Senha incorreta. Leia atentamente a segregação do valor do imóvel.")

    # FASE 4
    if st.session_state.fase >= 3:
        st.markdown("---")
        st.header("🏦 Sala 4: O Acerto de Contas")
        st.info("**Fato 12:** Os sócios integralizaram 40% dos seus compromissos pendentes (o que deviam na Sala 1) via banco.")
        resp4 = st.number_input("Qual o valor exato do débito que deve ser feito na conta 'Bancos Conta Movimento' neste fato?", min_value=0, step=1000, key="r4")
        
        if st.button("Destravar Sala Final"):
            if resp4 == 16000:
                st.balloons()
                st.success("🎉 PARABÉNS! Você escapou da sala e garantiu que o Balanço vai bater!")
            else:
                st.error("Senha incorreta. Calcule 40% sobre o saldo que estava pendente na Sala 1.")
else:
    st.warning("Por favor, selecione seu nome/equipe para iniciar o jogo.")
