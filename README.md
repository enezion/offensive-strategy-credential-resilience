📄 1. Arquivo: README.md (O Documento Mestre) 

Cybersecurity Challenge: Auditoria de Resiliência de Credenciais (RCHLO & DIO)

Introdução e Contextualização Estratégica

No atual panorama de ameaças, a persistência de vulnerabilidades de autenticação legadas representa uma negligência na higiene básica de segurança. Ataques de força bruta e as suas variantes modernas continuam a ser vetores primários de intrusão, explorando a previsibilidade do comportamento humano.  
Este projeto documenta a eficácia da ferramenta Medusa na identificação de credenciais fracas nos protocolos FTP, SMB e interfaces Web. A simulação destes ataques serve como uma métrica crítica para a resiliência da infraestrutura.


2. Metodologia e Configuração do Ambiente
3. Para garantir a integridade operacional e evitar impactos em sistemas de produção, a auditoria foi conduzida em ambiente controlado de sandboxing.  


Sistema Atacante: Kali Linux (Distribuição especializada em testes de intrusão).  


Alvos Vulneráveis: Metasploitable 2 (Serviços FTP/SMB) e DVWA (Simulador de vulnerabilidades web).  


Configuração de Rede: Rede isolada "Host-Only" via VirtualBox para contenção de tráfego.

3. Taxonomia de Ataques de Autenticação
A seleção da técnica de ataque é estratégica, visando maximizar o sucesso enquanto minimiza o ruído detectável por sistemas de monitoramento.

Técnica,Descrição,Aplicação Estratégica
Dicionário,Uso de listas de senhas pré-definidas.  ,Ataque de alta velocidade focado em termos comuns.  
Híbrido,Dicionário combinado com Regras de Mangling.  ,"Identifica variações complexas como ""P@ssw0rd123!"".  "
Password Spraying,Uma senha comum testada contra muitos usuários.  ,Crítico: Evita bloqueios de conta (Lockout).  

4. Execução e ResultadosProtocolo FTP: Através do Medusa, identificou-se a credencial service_admin - Pass: 123456, permitindo potencial exfiltração de dados.  Protocolo SMB: Execução de Password Spraying para simular movimentação lateral e coleta de informações de GPOs.  Interface Web (DVWA): Ataque parametrizado interpretando a string "Login failed" para validar o sucesso.

5. Matriz de Mitigação e ROI de Segurança
As descobertas confirmam que falhas de configuração (misconfigurations) são mais críticas que vulnerabilidades de software. 

   Prioridade,Medida de Segurança,Impacto
ALTA,Multi-Factor Authentication (MFA),Neutraliza 99% dos ataques de força bruta e spraying.  
ALTA,Account Lockout Policy,Bloqueia contas após N tentativas falhas.  
MÉDIA,SIEM & Logging Progressivo,Detecta padrões de login anômalos em tempo real.  
