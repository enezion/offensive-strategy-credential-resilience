# Sumário Executivo: Auditoria de Segurança Ofensiva

## Visão Geral
[cite_start]A auditoria identificou que a segurança da infraestrutura é altamente dependente da robustez das credenciais de utilizadores e serviços[cite: 280]. [cite_start]Falhas de configuração (*misconfigurations*) permitiram
o comprometimento de protocolos críticos em poucos minutos de simulação[cite: 308, 329]
2. [cite_start]**Exposição de SMB:** A ausência de políticas de bloqueio permitiu ataques de *Password Spraying* sem detecção[cite: 297, 312].
3. [cite_start]**Fragilidade Web:** Interfaces de login sem Múltiplo Fator de Autenticação (MFA) facilitam a intrusão automatizada[cite: 318, 332].

## Recomendação Estratégica (ROI)
[cite_start]A implementação imediata de **MFA** e de uma **Política de Bloqueio de Contas** neutraliza a eficácia de ferramentas como o Medusa em 99% dos cenários testados[cite: 332]. [cite_start]O custo destas medidas é marginal face ao potencial prejuízo de um incidente de *Ransomware*[cite: 333].
