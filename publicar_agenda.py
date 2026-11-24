import os
import subprocess
from datetime import datetime

def publicar_no_github():
    pasta_projeto = os.path.dirname(os.path.abspath(__file__))
    os.chdir(pasta_projeto)

    if not os.path.exists("agenda.json"):
        print("Erro: agenda.json não encontrado.")
        return

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
    msg = f"Atualizacao de agenda ({timestamp})"

    comandos = [
        "git add agenda.json",
        f'git commit -m "{msg}"',
        "git push"
    ]

    for cmd in comandos:
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if proc.returncode != 0:
            saida = proc.stderr or proc.stdout
            if "nothing to commit" in saida:
                print("Nenhuma alteração nova no agenda.json.")
            else:
                print(f"Erro ao executar '{cmd}':\n{saida}")
            return

    print("Sucesso! Site atualizado no GitHub Pages.")

if __name__ == "__main__":
    publicar_no_github()