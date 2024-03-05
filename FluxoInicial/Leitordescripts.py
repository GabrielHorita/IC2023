import subprocess


scripts = {
    "Script 1(Graf5)": "/Users/horita/Desktop/6LI /EDIT-GRAF5.py",
    "Script 2(Graf(6)": "/Users/horita/Desktop/6LI /EDIT-GRAF6.py",
    "Script 3(Graf7)": "/Users/horita/Desktop/6LI /Graf7edit.py",
    "Script 4(Graf8Pontilhado)": "/Users/horita/Desktop/6LI /Graf8linha-pontilhada.py",
    "Script 5(Graf8Continuo)": "/Users/horita/Desktop/6LI /Graf8-linhacontinua.py",
    "Script 6(Graf9)": "/Users/horita/Desktop/6LI /EDIT-GRAF9.py",
}


print("Escolher entre as opcoes:")
for i, (nome, _) in enumerate(scripts.items(), 1):
    print(f"{i}. {nome}")


opcao = int(input("Digite o numero do codigo que ira ser executado: "))


if opcao < 1 or opcao > len(scripts):
    print("Opção que nao esta adicionada !")
else:

    caminho_script = list(scripts.values())[opcao - 1]





    subprocess.run(["python", caminho_script])
