"""Teste rápido do Agente SEO no terminal.

Rastreamento de Execução:
    1. Importa o agente configurado de agente.py
    2. Envia um prompt de teste
    3. O agente pesquisa na web → gera o artigo → imprime no terminal

Uso:
    uv run python main.py
"""

from agente import agente_seo


def main() -> None:
    """Executa um teste do agente com um prompt de exemplo."""
    try:
        agente_seo.print_response(
            "Escreve um artigo sobre "
            "'Como Usar IA para Melhorar o SEO do Seu Site em 2026'"
        )
    except Exception as e:
        # Erros possíveis: API key inválida, modelo indisponível, sem internet
        print(f"❌ Erro ao executar o agente: {e}")
        print("💡 Verifica se a GOOGLE_API_KEY no .env está correta.")


if __name__ == "__main__":
    main()
