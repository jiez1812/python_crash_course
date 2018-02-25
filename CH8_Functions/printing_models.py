# Start with some designs that need to be printed.

def print_models(unprinted_designs, completed_models):
    # Simulate printing each design, until none are left.
    # Move each design to compleated_models after printint.
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: {0}".format(current_design))
        completed_models.append(current_design)

def show_completed_models(completed_models):
    # Display all completed models.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)