import numpy as np
import matplotlib.pyplot as plt

def plot_vector_field(f, xmin, xmax, ymin, ymax, xstep, ystep, field_type='F', streamlines=False, density=1.0):
    """
    Grafica el campo de direcciones de una EDO dy/dx = f(x, y)
    
    Parameters:
    -----------
    f : function
        Función f(x, y) de la EDO dy/dx = f(x, y)
    xmin, xmax : float
        Límites del eje x
    ymin, ymax : float
        Límites del eje y
    xstep, ystep : float
        Separación entre puntos en la malla
    field_type : str, optional
        'F' para campo completo, 'N' para campo unitario
    streamlines : bool, optional
        True para graficar líneas de flujo
    density : float, optional
        Densidad de las líneas de flujo (solo si streamlines=True)
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        Figura con el campo de direcciones
    """
    
    # Crear la malla de puntos
    x = np.arange(xmin, xmax + xstep, xstep)
    y = np.arange(ymin, ymax + ystep, ystep)
    X, Y = np.meshgrid(x, y)
    
    # campo vectorial
    if field_type == 'F':
        # campo completo: F(x, y) = (1, f(x, y))
        U = np.ones_like(X)
        V = f(X, Y)
    elif field_type == 'N':
        # Campo unitario: N(x, y) = (1, f(x, y)) / sqrt(1 + f(x, y)^2)
        V_temp = f(X, Y)
        magnitude = np.sqrt(1 + V_temp**2)
        U = 1 / magnitude
        V = V_temp / magnitude
    else:
        raise ValueError("field_type debe ser 'F' o 'N'")
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Graficar el campo de direcciones
    ax.quiver(X, Y, U, V, color='blue', angles='xy', scale_units='xy', scale=1, width=0.005)
    

    if streamlines:
        x_dense = np.linspace(xmin, xmax, 100)
        y_dense = np.linspace(ymin, ymax, 100)
        X_dense, Y_dense = np.meshgrid(x_dense, y_dense)
        
        V_dense = f(X_dense, Y_dense)
        if field_type == 'F':
            U_dense = np.ones_like(X_dense)
        else:
            V_temp_dense = f(X_dense, Y_dense)
            magnitude_dense = np.sqrt(1 + V_temp_dense**2)
            U_dense = 1 / magnitude_dense
            V_dense = V_temp_dense / magnitude_dense
        
        ax.streamplot(X_dense, Y_dense, U_dense, V_dense, color='red', density=density, linewidth=1.5)
    
    # grafico
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Campo de direcciones: dy/dx = f(x, y)\nTipo: {field_type}')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    
    return fig