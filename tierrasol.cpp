// SISTEMA SOLAR
// PLANETAS ALREDEDOR DEL SOL
//SOL-MERCURIO-VENUS-TIERRA-MARTE-JÚPITER

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

// Constantes
const double G = 6.67430e-11;  // Constante gravitacional (m^3 kg^-1 s^-2)
const double M = 1.989e30;     // Masa del Sol (kg)
const double dt = 100.0;       // Paso de tiempo (segundos)
const double AU = 1.496e11;    // Unidad astronómica (m)

// Estructura para almacenar el tiempo y posición de los planetas
struct DataPoint {
    double t;
    double x_mercurio;
    double y_mercurio;
    double x_venus;
    double y_venus;    
    double x_tierra;
    double y_tierra;
    double x_marte;
    double y_marte;
    double x_jupiter;
    double y_jupiter;
};

void simulate(double t_max) {
    // Crear un vector dinámico para almacenar los resultados
    std::vector<DataPoint> data;
    
    // Condiciones iniciales (MERCURIO - SOL)
    double x_mercurio = 0.387*AU;      // Posición inicial en x (1 AU)
    double y_mercurio = 0.0;     // Posición inicial en y
    double vx_mercurio = 0.0;    // Velocidad inicial en x
    double vy_mercurio = 47872;  // Velocidad inicial en y (m/s)

    // Condiciones iniciales (VENUS - SOL)
    double x_venus = 0.723*AU;      // Posición inicial en x (1 AU)
    double y_venus = 0.0;     // Posición inicial en y
    double vx_venus = 0.0;    // Velocidad inicial en x
    double vy_venus = 35021;  // Velocidad inicial en y (m/s)

    // Condiciones iniciales (TIERRA - SOL)
    double x_tierra = AU;      // Posición inicial en x (1 AU)
    double y_tierra = 0.0;     // Posición inicial en y
    double vx_tierra = 0.0;    // Velocidad inicial en x
    double vy_tierra = 29780;  // Velocidad inicial en y (m/s)

    // Condiciones iniciales (MARTE - SOL)
    double x_marte = 1.524 * AU; // Posición inicial en x
    double y_marte = 0.0;        // Posición inicial en y
    double vx_marte = 0.0;       // Velocidad inicial en x
    double vy_marte = 24077;     // Velocidad inicial en y (m/s)

    // Condiciones iniciales (JUPITER - SOL)
    double x_jupiter = 5.204 * AU; // Posición inicial en x
    double y_jupiter = 0.0;        // Posición inicial en y
    double vx_jupiter = 0.0;       // Velocidad inicial en x
    double vy_jupiter = 13070;     // Velocidad inicial en y (m/s)

 
    // Resolución de la simulación
    for (double t = 0; t <= t_max; t += dt) {
        // Guardar datos en el vector
        data.push_back({t,x_mercurio, y_mercurio, x_venus, y_venus ,x_tierra, y_tierra, x_marte, y_marte, x_jupiter, y_jupiter});

//calculamos los radios de los planetas en función del sol
        // Calcular la distancia al Sol (MERCURIO-SOL)
        double rm = std::sqrt(x_mercurio * x_mercurio + y_mercurio * y_mercurio);

        // Calcular la distancia al Sol (VENUS-SOL)
        double rv = std::sqrt(x_venus * x_venus + y_venus * y_venus);
	
        // Calcular la distancia al Sol (TIERRA-SOL)
        double rt = std::sqrt(x_tierra * x_tierra + y_tierra * y_tierra);

        // Calcular la distancia al Sol (MARTE-SOL)
        double rmm = std::sqrt(x_marte * x_marte + y_marte * y_marte);

        // Calcular la distancia al Sol (JUPITER-SOL)
        double rj = std::sqrt(x_jupiter * x_jupiter + y_jupiter * y_jupiter);



//calculamos las aceleraciones de los planetas alrededor del sol	
        // Calcular aceleraciones (MERCURIO-SOL)
        double axm = -G * M * x_mercurio / (rm * rm * rm);
        double aym = -G * M * y_mercurio / (rm * rm * rm);

        // Calcular aceleraciones (VENUS-SOL)
        double axv = -G * M * x_venus / (rv * rv * rv);
        double ayv = -G * M * y_venus / (rv * rv * rv);
	
        // Calcular aceleraciones (TIERRA-SOL)
        double axt = -G * M * x_tierra / (rt * rt * rt);
        double ayt = -G * M * y_tierra / (rt * rt * rt);
	
        // Calcular aceleraciones (MARTE-SOL)
        double axmm = -G * M * x_marte / (rmm * rmm * rmm);
        double aymm = -G * M * y_marte / (rmm * rmm * rmm);

        // Calcular aceleraciones (JUPITER-SOL)
        double axj = -G * M * x_jupiter / (rj * rj * rj);
        double ayj = -G * M * y_jupiter / (rj * rj * rj);
	 
//calculamos las posiciones de los planetas alrededor del sol
        //MERCURIO
	// Actualizar velocidades 
        vx_mercurio += axm * dt;
        vy_mercurio += aym * dt;

        // Actualizar posiciones 
        x_mercurio += vx_mercurio * dt;
        y_mercurio += vy_mercurio * dt;

	//VENUS
        // Actualizar velocidades 
        vx_venus += axv * dt;
        vy_venus += ayv * dt;

        // Actualizar posiciones
        x_venus += vx_venus * dt;
        y_venus += vy_venus * dt;

        //TIERRA
	// Actualizar velocidades 
        vx_tierra += axt * dt;
        vy_tierra += ayt * dt;

        // Actualizar posiciones 
        x_tierra += vx_tierra * dt;
        y_tierra += vy_tierra * dt;

	//MARTE
        // Actualizar velocidades 
        vx_marte += axmm * dt;
        vy_marte += aymm * dt;

        // Actualizar posiciones
        x_marte += vx_marte * dt;
        y_marte += vy_marte * dt;

	//JUPITER
        // Actualizar velocidades 
        vx_jupiter += axj * dt;
        vy_jupiter += ayj * dt;

        // Actualizar posiciones
        x_jupiter += vx_jupiter * dt;
        y_jupiter += vy_jupiter * dt;
    }

    // Guardar en archivo
    std::ofstream file("orbitas.csv");
    file << "t,x_mercurio,y_mercurio,x_venus,y_venus, x_tierra, y_tierra, x_marte, y_marte, x_jupiter,y_jupiter\n";
    for (const auto& point : data) {
        file << point.t << "," << point.x_mercurio << "," << point.y_mercurio << "," << point.x_venus << "," << point.y_venus <<
	  "," << point.x_tierra << "," << point.y_tierra << "," << point.x_marte << "," << point.y_marte <<"," << point.x_jupiter <<
	  "," << point.y_jupiter << "\n";
    }

    file.close();
    std::cout << " Resultados guardados en 'orbitas.csv'.\n";
}

int main() {
    double t_max = 365.25 * 24 * 3600;  // Tiempo de simulación (2 años en segundos)
    simulate(t_max);
    return 0;
}
