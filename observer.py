class Observer:
   
    def update(self, device):
        print(f'a {device.type} was added to the smart house.')

    def update_remove(self, device):
        print(f'a {device.type} was removed from the smart house.')