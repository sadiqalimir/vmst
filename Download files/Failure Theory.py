import tkinter as tk
import math
from tkinter import messagebox


#define failure theories as functions
def rankine(yield_strength,stress):
     
    safety_factor = yield_strength / stress
    if safety_factor < 1:
        return  "The material fails according to Rankine's theory."
    else:
        return   "The material does not fail according to Rankine's theory."


def venant(sigma_x,sigma_y,yield_strength,tau_xy):
    principal_stress_1 = ((sigma_x + sigma_y)/2) + math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
    principal_stress_2 = ((sigma_x + sigma_y)/2) - math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
    safety_factor_1 = yield_strength / principal_stress_1
    safety_factor_2 = yield_strength / principal_stress_2
    if safety_factor_1 < 1 or safety_factor_2 < 1:
        return "The material has failed by St. Venant's theory."
    else:
        return "The material has not failed by St. Venant's theory."

def guest(sigma_x,sigma_y,yield_strength,tau_xy):
   
    principal_stress_1 = ((sigma_x + sigma_y)/2) + math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
    principal_stress_2 = ((sigma_x + sigma_y)/2) - math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)


    stress_sum = principal_stress_1 + principal_stress_2
    stress_difference = abs(principal_stress_1 - principal_stress_2)
    safety_factor = yield_strength / (stress_sum + stress_difference)
    if safety_factor < 1:
        return "The material has failed by J. J. Guest's theory."
    else:
        return "The material has not failed by J. J. Guest's theory."

def haigh(stress_amplitude,fatigue_limit):
    if stress_amplitude < fatigue_limit:
        return "The material has not failed by Haigh's theory."
    else:
        return "The material has failed by Haigh's theory!"

def von_mises(sigma_x,sigma_y,yield_strength,tau_xy):
    #calculate principle stresses
    principal_stress_1 = ((sigma_x + sigma_y)/2) + math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
    principal_stress_2 = ((sigma_x + sigma_y)/2) - math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)

    # Calculate the von Mises stress for biaxial loading
    von_mises = math.sqrt(principal_stress_1**2 + principal_stress_2**2 - principal_stress_1*principal_stress_2)

    # Compare to yield stress
    if von_mises > yield_strength:
        return "Material fails according to von Mises criterion."
    else:
        return "Material is safe according to von Mises criteria."


#ui window
root = tk.Tk()
root.title("Material Failure Calculator")

canvas = tk.Canvas(root, height = 500, width = 500)
canvas.pack()


 


frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

stress_label = tk.Label(frame, text="Stress (KPa):",bg='#e6f5ff')
stress_label.place(relx=0,rely=0,relwidth=0.5,relheight=0.1)
stress_entry = tk.Entry(frame)
stress_entry.place(relx=0.5,rely=0,relwidth=0.5,relheight=0.1)

sigma_x_label = tk.Label(frame,text="Load in x-direction (Kpa)",bg='#e6f5ff')
sigma_x_label.place(relx=0,rely=0.1,relwidth=0.5,relheight=0.1)
sigma_x_entry = tk.Entry(frame)
sigma_x_entry.place(relx=0.5,rely=0.1,relwidth=0.5,relheight=0.1)

sigma_y_label = tk.Label(frame,text="Load in y-direction (Kpa)",bg='#e6f5ff')
sigma_y_label.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.1)
sigma_y_entry = tk.Entry(frame)
sigma_y_entry.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.1)


tau_xy_label = tk.Label(frame,text="shear stress along x-y (Kpa)",bg='#e6f5ff')
tau_xy_label.place(relx=0,rely=0.3,relwidth=0.5,relheight=0.1)
tau_xy_entry = tk.Entry(frame)
tau_xy_entry.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.1)

yield_strength_label = tk.Label(frame, text="Yield Strength (KPa):",bg='#e6f5ff')
yield_strength_label.place(relx=0,rely=0.4,relwidth=0.5,relheight=0.1)
yield_strength_entry = tk.Entry(frame)
yield_strength_entry.place(relx=0.5,rely=0.4,relwidth=0.5,relheight=0.1)

fatigue_limit_label = tk.Label(frame, text="Fatigue Limit (KPa):",bg='#e6f5ff')
fatigue_limit_label.place(relx=0,rely=0.5,relwidth=0.5,relheight=0.1)
fatigue_limit_entry = tk.Entry(frame)
fatigue_limit_entry.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.1)

stress_amplitude_label = tk.Label(frame, text="Stress Amplitude (KPa):",bg='#e6f5ff')
stress_amplitude_label.place(relx=0,rely=0.6,relwidth=0.5,relheight=0.1)
stress_amplitude_entry = tk.Entry(frame)
stress_amplitude_entry.place(relx=0.5,rely=0.6,relwidth=0.5,relheight=0.1)

def check_failure():
    yield_strength = int(yield_strength_entry.get())
    stress = int(stress_entry.get())
    sigma_x = int(sigma_x_entry.get())
    sigma_y = int(sigma_y_entry.get())
    tau_xy = int(tau_xy_entry.get())
    fatigue_limit = int(fatigue_limit_entry.get())
    stress_amplitude = int(stress_amplitude_entry.get())
    
    rankine_result = rankine(stress, yield_strength)
    venant_result = venant(sigma_x,sigma_y,tau_xy, yield_strength)
    guest_result = guest(sigma_x,sigma_y,tau_xy,yield_strength)
    haigh_result = haigh(fatigue_limit, stress_amplitude)
    von_mises_result = von_mises(sigma_x,sigma_y,tau_xy, yield_strength)




# Display the results in a message box
    results_text = f"{rankine_result}\n{venant_result}\n{guest_result}\n{haigh_result}\n{von_mises_result}"
    tk.messagebox.showinfo(title="Results", message=results_text)

check_button = tk.Button(frame, text="Check Failure", command=check_failure)
check_button.place(relx=0.35,rely=0.75,relwidth=0.4,relheight=0.2)



root.mainloop()
