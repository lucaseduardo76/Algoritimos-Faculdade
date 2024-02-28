from cx_Freeze import setup, Executable

setup(
    name="Gerenciador de Tarefas",
    version="1.0",
    description="Programa que auxilia na gestão de funcionarios",
    executables=[Executable("sistemaTarefas.py")],
)