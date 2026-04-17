🚜 Script de Automação de Fazenda (Python)

📋 Descrição do Projeto
Este projeto consiste em um sistema de automação para colheita e plantio em larga escala (4 Fazendas com 16 terrenos em cada). O script utiliza visão por coordenadas e técnicas de simulação humana para percorrer o mapa, desmontar da montaria, realizar o trabalho agrícola, subir na montaria e seguir para o próximo lote de forma cíclica.

🎯 Escopo e Funcionalidades
Navegação Dinâmica: Movimentação baseada em Waypoints para contornar a impossibilidade de clique direto no minimapa e garantir uma maior precisão e eficiência na navegação.

Ciclo de Trabalho Completo: Caminha até o Terreno -> Executa Colheita -> Pega Semente -> Executa Plantio -> Volta a Montaria

Gestão de Montaria: Sistema de "Checkpoints" para garantir que o boneco suba na montaria sempre na mesma posição, evitando erros de direção durante a navegação entre terrenos.

Humanização: Intervalos de tempo aleatórios (random.uniform) em todas as ações para reduzir o risco de detecção de script/macro.

🚦 Status do Desenvolvimento

✅ Concluído

[x] Estrutura base do Loop principal.

[x] Funções de Colheita com suporte a tecla Shift.

[x] Lógica de randomização de milissegundos.

[x] Mapeamento de coordenadas dos terrenos da primeira e segunda fazenda.

[x] Sistema de correção de ângulo da montaria (Ponto de Reset).

[x] Função de plantação.

[x] Função de navegação entre Terrenos na 1º e 2º fazenda.

[x] Função para identificar Coordenadas X e Y na tela.

[x] Implementar condição para trocar tipo de semente de acordo com o terreno na 2º fazenda.

[x] Função para navegar até o sistema de armazenamento e guardar itens colhidos da 1º fazenda.

[x] Função para navegar até a 2º fazenda, pegar montaria, semente e posicionar no ponto de colheita.

🚧 Em Desenvolvimento (Pendente)

[ ] Mapear coordenadas de navegação para a 3º e 4º fazenda.

[ ] Mapear pontos de "embarque" da montaria para 3º fazenda devido a diferença no terreno.

[ ] Implementar função para ordenhar vacas e alimentar as mesmas na 3º fazenda.

🛠️ Tecnologias Utilizadas
Python 3.10+

PyAutoGUI: Biblioteca utilizada para controle do mouse e teclado.

Random/Time: Para simulação de comportamento humano.

🔧 Como Configurar para Testes
Resolução do Jogo: 1920x800 (Modo Janela sem bordas).

Atalhos: - Tecla A: Montar/Desmontar.

Tecla I: Abrir Inventário.

Tecla Shift: Manter para colheita rápida.

Calibração: Caso o boneco erre o clique, atualizar as listas spotColeta, posicaoMontaria, spotPlantacao e caminhoTerrenos com as novas coordenadas (x, y).

⚠️ Avisos de Segurança
O bot possui o sistema FAILSAFE do PyAutoGUI ativo. Caso o bot perca o controle, arraste o mouse rapidamente para qualquer um dos quatro cantos da tela para forçar a paragem imediata.

💡 Dica para o Futuro
Este projeto pode ser expandido com OpenCV para identificar automaticamente se a planta está no estado de colheita antes de iniciar o ciclo, tornando-o 100% inteligente.
