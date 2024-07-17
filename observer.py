class Observer:
   
    def update(self, **kwargs):
        device = kwargs['device']
        operation = kwargs['operation']
        state = kwargs.get('state', None)
        if operation == 'add':
            print(f"You added a {device} to the smart house.")
        elif operation == 'remove':
            print(f"You removed a {device} from the smart house.")
        else:
            print(f"The {device} changed its state to {state}.")
        
