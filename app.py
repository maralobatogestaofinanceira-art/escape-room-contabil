import streamlit as st

# Configuração da página
st.set_page_config(page_title="Escape Room: Monitoria de Contabilidade", page_icon="🔐")

# --- CONTROLE DE ACESSO ---
alunos_permitidos = ["Selecione...", "Equipe 1", "Equipe 2", "Equipe 3"]

st.title("🔐 Escape Room Contábil")
st.markdown("Bem-vindos à atividade de Monitoria de Contabilidade Básica I da UFRN! A missão de hoje é fechar as contas, seguindo o raciocínio desde o Livro Diário até ao Balanço Patrimonial.")

# Variáveis de controle de fase
if 'fase' not in st.session_state:
    st.session_state.fase = 0

usuario = st.selectbox("Identifique-se para aceder:", alunos_permitidos)

if usuario != "Selecione...":
    st.success(f"Acesso liberado para: {usuario}")
    
    # FASE 1: DIÁRIO
    if st.session_state.fase >= 0:
        st.header("📖 Sala 1: O Livro Diário")
        st.info("A primeira etapa é registar os 12 eventos. Para provar que dominaram os registos iniciais...")
        resp1 = st.number_input("Somando apenas as compras dos Eventos 2, 4 e 7, qual o valor total debitado na conta 'Mercadorias'?", min_value=0, step=1000, key="r1")
        
        if st.button("Destrancar Sala 1"):
            if resp1 == 36000:
                st.session_state.fase = max(st.session_state.fase, 1)
                st.success("Cadeado aberto! O total de aquisições de mercadorias é R$ 36.000,00.")
            else:
                st.error("Valor incorreto. Revejam os lançamentos das compras a prazo e a pronto.")

    # FASE 2: RAZÃO
    if st.session_state.fase >= 1:
        st.markdown("---")
        st.header("⚖️ Sala 2: Os Razonetes")
        st.info("Depois de escriturar no Razão, é crucial verificar a liquidez da empresa.")
        resp2 = st.number_input("Considerando as entradas e saídas de todos os factos, qual é o saldo final da conta 'Bancos Conta Movimento'?", min_value=0, step=1000, key="r2")
        
        if st.button("Destrancar Sala 2"):
            if resp2 == 55500:
                st.session_state.fase = max(st.session_state.fase, 2)
                st.success("Cadeado aberto! O saldo exato é R$ 55.500,00.")
            else:
                st.error("Incorreto. Revejam as entradas (Eventos 1, 6, 12) e saídas (Eventos 4, 9).")

    # FASE 3: BALANCETE
    if st.session_state.fase >= 2:
        st.markdown("---")
        st.header("📊 Sala 3: O Balancete de Verificação")
        st.info("O somatório de saldos devedores deve bater com os credores. Vamos focar-nos nas rubricas de resultado.")
        resp3 = st.number_input("Qual é o saldo credor total (somatório) da conta 'Receita de Vendas' antes do fecho?", min_value=0, step=1000, key="r3")
        
        if st.button("Destrancar Sala 3"):
            if resp3 == 28000:
                st.session_state.fase = max(st.session_state.fase, 3)
                st.success("Cadeado aberto! A receita total apurada é R$ 28.000,00.")
            else:
                st.error("Incorreto. Somem apenas os valores de venda das mercadorias.")

    # FASE 4: DRE
    if st.session_state.fase >= 3:
        st.markdown("---")
        st.header("📈 Sala 4: A Demonstração do Resultado (DRE)")
        st.info("Com a Receita validada, sabemos pelos razonetes que o CMV (Custo das Mercadorias Vendidas) totalizou R$ 20.250,00.")
        resp4 = st.number_input("Deduza o CMV das Receitas. Qual é o valor exato do Resultado (Lucro) a ser transferido para o PL?", min_value=0, step=100, key="r4")
        
        if st.button("Destrancar Sala 4"):
            if resp4 == 7750:
                st.session_state.fase = max(st.session_state.fase, 4)
                st.success("Cadeado aberto! Lucro de R$ 7.750,00 apurado com sucesso.")
            else:
                st.error("Incorreto. A matemática da DRE é simples: Receita Líquida menos Custos.")

    # FASE 5: BALANÇO PATRIMONIAL
    if st.session_state.fase >= 4:
        st.markdown("---")
        st.header("🏛️ Sala Final: O Balanço Patrimonial")
        st.info("O momento da verdade para a Professora Gilmara aprovar o exercício! Juntem o Lucro às contas patrimoniais.")
        resp5 = st.number_input("Qual é o valor exato do TOTAL DO ATIVO (que iguala o Passivo + PL) no encerramento?", min_value=0, step=1000, key="r5")
        
        if st.button("Destrancar Sala Final"):
            if resp5 == 232750:
                st.balloons()
                st.success("🎉 PARABÉNS! Escaparam do labirinto e o Balanço fechou na perfeição!")
            else:
                st.error("Incorreto. Verifiquem o somatório do Ativo Circulante e Não Circulante.")
else:
    st.warning("Por favor, selecione a sua equipa para iniciar o jogo.")
