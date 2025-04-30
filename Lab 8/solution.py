# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import control as cntrl

# making an object for the systems
system = [{"label" :"G1","num" :[1] ,"den" :[1,0]},
          {"label" :"G2","num" :[1,0] ,"den" :[1]},
          {"label" :"G3","num" :[1] ,"den" :[1,0,0]},
          {"label" :"G4","num" :[1,0,0] ,"den" :[1]},
          {"label" :"G5","num" :[1] ,"den" :[1,1]},
          {"label" :"G6","num" :[1] ,"den" :[0,1]},
          {"label" :"G7","num" :[1] ,"den" :[0.1,0]},
          {"label" :"G8","num" :[0.1,1] ,"den" :[10,1]},
          {"label" :"G9","num" :[30,300] ,"den" :[1,3,50]}
         ]


subplot=1;
# loop over each system
for sys in system:
    # define numerator and denominator of each transfer function by taking the respective keys from 
    numerator =sys['num']
    denominator=sys['den']
    # defining the transfer function using python's 'control' library
    system=cntrl.TransferFunction(numerator,denominator)

    # make an array of frequencies
    frequencies = np.array([0.01,0.1,1,10,100])
    # get the magnitude, phase and omega from cntrl.bode function
    mag,phase,omega=cntrl.bode(system,frequencies,db = True,plot=False)

    gain_db=20*np.log(mag)  # convert the parameters to required form
    phase_deg=np.degrees(phase)


    print("Frequency (rad/s) | Gain (dB) | Phase (degrees)")
    for f, g, p in zip(omega, gain_db, phase_deg):
        print(f"{f:<18} {g:<10.2f} {p:<.2f}")

    plt.figure(figsize=(20,40))
    plt.subplot(9,2,subplot)
    subplot+=1
    plt.semilogx(omega, gain_db, 'o-', label='Gain (dB)')
    plt.xlabel('Frequency (rad/sec)')
    plt.ylabel('Gain (dB)')
    plt.title(f"Magnitude Plot for {sys['label']}")
    plt.grid(True)
    plt.legend()

    plt.subplot(9,2,subplot)
    subplot+=1
    
    plt.semilogx(omega, phase_deg, 's-', color = "orange", label='Gain (dB)')
    plt.xlabel('Frequency (rad/sec)')
    plt.ylabel('Gain (dB)')
    plt.title(f"phase Plot {sys['label']}")
    plt.grid(True)
    plt.legend()


plt.tight_layout()
plt.show()