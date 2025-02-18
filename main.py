from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class MeuGame(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        # Definindo cor do background
        self.set_background_color(0, 50, 50)
        # Carregando modelo de ambiente
        self.scene = self.loader.loadModel("models/pada3d1.bam")
        # Reparentando o modelo para renderizar
        self.scene.reparentTo(self.render)
        # Alterando a escala da cena
        self.scene.setScale(0.75, 0.75, 0.75)
        # Definindo a posição do modelo
        self.scene.setPos(-10, 50, 2)
        # Adicionando o procedimento cameraTask ao gerenciador de tarefas
        self.task_mgr.add(self.cameraTask, "cameraTask")
        # Definindo o procedimento de movimento  da camera

    def cameraTask(self, task):
        # Gerando um angulo de acordo com o tempo
        angleDegrees = task.time * 5.0
        # Convertendo o angulo em radianos
        angleRadius = angleDegrees * (pi / 180)
        # Definindo a posição da câmera
        self.camera.setPos(20 * sin(angleRadius), -20 * cos(angleRadius), 2)
        # Dando uma assinatura a câmera
        self.camera.setHpr(angleRadius, 0, 0)

        # retornando a contagem
        return Task.cont


app = MeuGame()
app.run()
