# 🍅 Pomodoro CLI

Uma ferramenta de linha de comando simples e elegante para aplicar a técnica Pomodoro, ajudando você a manter o foco e produtividade.

## ✨ Funcionalidades

- **Ciclos de Foco**: Sessões de 25 minutos de trabalho concentrado
- **Pausas Automáticas**: Intervalos de 5 minutos após cada sessão
- **Contagem Regressiva Visual**: Display colorido com tempo restante
- **Notificações Desktop**: Alertas visuais e sonoros ao final de cada ciclo
- **Histórico de Sessões**: Acompanhe quantos ciclos você completou
- **Interface Rica**: Saída colorida e formatada com emojis

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone git@github.com:carloshendvpm/pomo-cli.git
cd pomo-cli
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📖 Como Usar

### Iniciar um Ciclo Pomodoro
```bash
python pomodoro.py start
```

Isso iniciará:
- 25 minutos de foco
- 5 minutos de descanso
- Notificação ao final de cada etapa

### Ver Histórico de Sessões
```bash
python pomodoro.py status
```

Mostra quantos ciclos Pomodoro você completou.

### Resetar Histórico
```bash
python pomodoro.py reset
```

Zera o contador de sessões completadas.

### Ajuda
```bash
python pomodoro.py --help
```

## 🛠️ Dependências

- **rich**: Interface colorida e formatada no terminal
- **plyer**: Notificações multiplataforma do sistema

## 📊 Técnica Pomodoro

A técnica Pomodoro é um método de gerenciamento de tempo que usa intervalos cronometrados para melhorar o foco e a produtividade:

1. **25 minutos** de trabalho concentrado
2. **5 minutos** de pausa
3. Repita o ciclo
4. A cada 4 ciclos, faça uma pausa mais longa (15-30 minutos)

## 🎯 Benefícios

- Melhora o foco e concentração
- Reduz a procrastinação
- Aumenta a produtividade
- Previne o burnout com pausas regulares
- Facilita o acompanhamento do progresso

## 🔧 Funcionalidades Técnicas

- Armazenamento local do histórico em JSON
- Notificações cross-platform
- Interface de linha de comando intuitiva
- Feedback visual e sonoro
- Tratamento de erros robusto