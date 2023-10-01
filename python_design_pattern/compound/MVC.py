class Model(object):
    services = {
        "email":{"number": 1000, "price": 2,},
        "sms": {"number": 1000, "price": 10,},
        "voice": {"number": 1000, "price": 15,},
    }


class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]["number"], svc, "message you pay $", Model.services[svc]["price"])


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
    

class Client(object):
    controller = Controller()
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()


"""
Services Provided:
email  
sms  
voice  
Pricing for Services:
For 1000 email message you pay $ 2
For 1000 sms message you pay $ 10
For 1000 voice message you pay $ 15
"""