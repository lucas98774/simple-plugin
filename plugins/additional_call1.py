from my_app import factory

def additional_call1() -> None:
    print("This is a plugin call which is better! I allow for extension!")
    return

def register() -> None:
    factory.register("additional call", additional_call1)
    return