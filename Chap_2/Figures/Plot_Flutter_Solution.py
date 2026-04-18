import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    print("This script plots the function: h0(t) = e^(a*t) * sin(b*t)")
    
    # Get user input for parameters 'a' and 'b'
    try:
        a = float(input("Enter the value for 'a' (e.g., -0.5 for damping, 0.5 for growth): "))
        b = float(input("Enter the value for 'b' (frequency parameter, e.g., 5): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        sys.exit(1)

    # Define the time array 't' from 0 to 10 with 1000 points for a smooth curve
    t = np.linspace(0, 10, 1000)

    # Calculate the amplitude 'h0' based on the given formula
    h0 = np.exp(a * t) * np.sin(b * t)
    
    # Calculate the individual components
    envelope = np.exp(a * t)
    sine_wave = np.sin(b * t)

    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot the individual components with transparency
    plt.plot(t, envelope, color='red', alpha=0.4, linestyle='--', label=rf'$e^{{{a}t}}$')
    plt.plot(t, sine_wave, color='green', alpha=0.4, linestyle=':', label=rf'$\sin({b}t)$')

    # Plot the main combined data
    plt.plot(t, h0, color='blue', linewidth=2, label=rf'$e^{{{a}t}} \cdot \sin({b}t)$')
    
    # Set labels and title
    plt.xlabel('time (t)', fontsize=12)
    plt.ylabel('amplitude (h0)', fontsize=12)
    
    # Add a horizontal line at y=0 for reference
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    
    # Add grid and legend
    plt.grid(True, linestyle=':', alpha=0.7)
    # plt.legend(fontsize=12)
    plt.savefig('Flutter_Decay_Solution_Plot.png', dpi=300)  
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()