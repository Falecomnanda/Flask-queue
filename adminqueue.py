from twilio.rest import Client

class AdminQueue:
    def __init__(self):
        self.account_sid = 'AC2795129ff0be2462b79932fc3e91596a'
        self.auth_token = '65f5dcb6615319d3b9b35b3e8d95c247'
        self.client = Client(self.account_sid, self.auth_token)
        self._queue = []
        self._mode = 'FIFO'

    def enqueue(self, item):
        #### Aqui deben añadir a la cola ####
        self._queue.append(item)
        message = self.client.messages.create(
                              body='Bienvenido,'+ item ['name'] + ' usted sera atendido despues de '+ str(self.size()) + ' person!',
                              from_='+12038034771',
                              to=str(item['phone'])
                          )

        return message.sid                  
        #####################################
    def dequeue(self):
        #### Aqui deben procesar la cola ####
        if self.size() > 0:
            if self.mode == 'FIFO':
                item = self._queue.pop()
                return item
            elif self._mode == 'LIFO':
                item = self._queue.pop(-1)
                return item
        else:
            msg = {
                "msg": "Fila sin elementos"
            }
            return msg
        #####################################

    def get_queue(self):
        ####    Retornar Toda la Fila    ####
        return self._queue
        #####################################

    def size(self):
        return len(self._queue)