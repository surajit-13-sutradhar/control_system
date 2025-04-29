
for zero in zeroes:
    # defining the transfer function:= [(s - z[0])(s - z[1])] / [(s + 2)(s + 3)]
    G = ctrl.TransferFunction(np.polymul([1 , -zero[0]], [1 , -zero[1]]), np.polymul([1, 2], [1, 3]))
    t_out, y_out = ctrl.step_response(G, t)

    # plotting the graph
    # generating random colours
    random_colour = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    plt.plot(t_out, y_out, label="Step Response", color=random_colour)