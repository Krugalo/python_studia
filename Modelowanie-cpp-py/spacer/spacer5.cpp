#include<iostream>
#include<random>
#include<fstream>
#include<cstdlib>
#include<time.h>

int main( )
{
    srand(time(NULL));
    
    
    const int N = 1000;
    int krok_set = 1;
    int krok;
    int kierunek;
    int pozycja[3] = {};

    std::ofstream f;
    std::string name;
    name = "spacer5.txt";

    f.open(name);
    
    for (int i = 0; i < N; i++)
    {
        kierunek = rand( ) % 3;
        krok = rand( ) % 2 ? krok_set : -krok_set;
        
        pozycja[kierunek] += krok;

        f << pozycja[0] << ", " << pozycja[1] << ", " << pozycja[2] << '\n';
    }
    
    f.close( );
}