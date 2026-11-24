# 🎮 Portal de Agenda Automatizado — Ren Akabane

[![Live Demo](https://img.shields.io/badge/Demo-GitHub%20Pages-00f0ff?style=for-the-badge&logo=github)](https://ren-akabane.github.io/agenda-lives/)
[![Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20Tailwind%20%7C%20JS-ff0055?style=for-the-badge)]()
[![Automation](https://img.shields.io/badge/Automation-Python%20%7C%20n8n%20%7C%20WhatsApp%20API-25D366?style=for-the-badge)]()

Aplicação web responsiva e orientada a dados desenvolvida para gerenciar cronogramas de transmissões ao vivo, contagem regressiva em tempo real e acompanhamento de campanhas, utilizando uma arquitetura desacoplada com deploy contínuo gratuito via **GitHub Pages** e automação via **Python** e **n8n (ChatOps)**.

🔗 **Acesse em produção:** [https://ren-akabane.github.io/agenda-lives/](https://ren-akabane.github.io/agenda-lives/)

---

## 🏗️ Arquitetura da Solução

O projeto separa completamente a camada de apresentação (`index.html`) da camada de estado (`agenda.json`), permitindo atualizações em produção sem necessidade de editar código-fonte manualmente:

```text
[ Desktop: Script Python / .bat ] ──┐
                                    ├──► [ GitHub Repo (agenda.json) ] ──► [ GitHub Pages CDN ]
[ Mobile: WhatsApp + Agente n8n ] ──┘                                             │
                                                                                  ▼
                                                                     [ Frontend (index.html) ]
                                                                     (Fetch + Cache-Busting)
```

### Principais Componentes

1. **Frontend Dinâmico (`index.html`):**
   - Construído com **HTML5**, **Tailwind CSS** e **JavaScript Vanilla**.
   - Consumo assíncrono do arquivo `agenda.json` via `fetch` com parâmetros de *cache-busting* para garantir leitura imediata de atualizações.
   - Cálculo dinâmico de contagem regressiva sincronizado com o fuso horário de Brasília (`America/Sao_Paulo`, `UTC-3`), detecção automática de status *Ao Vivo / Offline* e renderização interativa de progresso de campanha.

2. **Camada de Dados (`agenda.json`):**
   - Arquivo estruturado em JSON que atua como *Single Source of Truth* (Fonte Única de Verdade) para os horários semanais e o progresso da campanha atual.

3. **Pipeline Local Automatizado (Python + Batch):**
   - Script de automação local mapeado para execução rápida em 1 clique que valida a integridade do JSON, executa o versionamento Git (`add`, `commit`) e realiza o `push` direto para a branch de produção.

4. **Agente Autônomo via WhatsApp (n8n + Meta Cloud API):**
   - Fluxo orquestrado no **n8n** integrado à **Meta WhatsApp Cloud API** e à **GitHub REST API**.
   - Permite atualizar o estado do site em linguagem natural pelo celular (ex.: *"Marca a live #1 como concluída"*). O agente de IA lê o `agenda.json` atual no repositório, modifica os booleanos correspondentes e realiza o commit automático.

---

## 📄 Estrutura do Schema (`agenda.json`)

```json
{
  "horarios_semanais": [
    {
      "day": 4,
      "name": "Quinta-feira",
      "startH": 21,
      "startM": 30,
      "durationMins": 150,
      "endLabel": "00:00"
    },
    {
      "day": 5,
      "name": "Sexta-feira",
      "startH": 21,
      "startM": 30,
      "durationMins": 210,
      "endLabel": "01:00"
    },
    {
      "day": 6,
      "name": "Sábado",
      "startH": 15,
      "startM": 0,
      "durationMins": 240,
      "endLabel": "19:00"
    }
  ],
  "campanha_atual": {
    "titulo": "PHANTOM BLADE ZERO:",
    "subtitulo": "JORNADA SUPREMA (NG+)",
    "lives_concluidas": [
      false,
      false,
      false,
      false,
      false,
      false,
      false,
      false,
      false
    ]
  }
}
```

### Dicionário de Dados

| Chave | Tipo | Descrição |
| :--- | :--- | :--- |
| `horarios_semanais[].day` | `Integer` | Dia da semana no padrão `Date.getDay()` (`0` = Domingo a `6` = Sábado). |
| `horarios_semanais[].startH` / `startM` | `Integer` | Hora e minuto de início da transmissão (horário de Brasília). |
| `horarios_semanais[].durationMins` | `Integer` | Duração prevista da transmissão em minutos (usada no cálculo de horas jogadas). |
| `campanha_atual.titulo` / `subtitulo` | `String` | Título e subtítulo exibidos dinamicamente no banner principal da campanha. |
| `campanha_atual.lives_concluidas` | `Array<Boolean>` | Lista sequencial que controla os marcos concluídos (`true`/`false`), porcentagem e horas acumuladas. |

---

## 🚀 Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/ren-akabane/agenda-lives.git
   cd agenda-lives
   ```

2. Como o projeto utiliza requisições `fetch()` para carregar o `agenda.json`, inicie um servidor HTTP local (ex.: com Python ou extensão *Live Server* no VS Code) para evitar bloqueios de CORS:
   ```bash
   python -m http.server 8000
   ```

3. Acesse `http://localhost:8000` no navegador.

---

## 👨‍💻 Autor

Desenvolvido por **Bruno de Souza Silva** (`@ren_akabane`) — Analista de Dados & Automação.

- **LinkedIn:** [Conecte-se comigo](https://www.linkedin.com/)
- **YouTube:** [@ren_akabane](https://www.youtube.com/@ren_akabane)