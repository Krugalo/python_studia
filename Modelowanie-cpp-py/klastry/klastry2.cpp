#include<iostream>
#include<random>
#include<cstdlib>
#include<fstream>
#include<time.h>
#include<vector>

//lista zwierająca pozycje
const int height = 100;
const int width = 100;
bool pole[width][height]; //pole zarodnikow
bool pole2[width][height]; //pole komorek

class Komorka
{
public:
    
    //wspolrzedne
    int x, y;

    void placement( )
    {
        //szuka pola o wartosci 0
        do
        {
            x = rand( ) % width;
            y = rand( ) % height;
        }
        while (pole[x][y] && pole2[width][height]);
    }
};



int main( )
{
    std::cout << "test 1" << '\n';
    
    //ilosc czastek
    const int N = 1000;

    //vektor na czastki
    std::vector<Komorka> czastki;
    Komorka k;
    
    //rand
    srand(time(NULL));

    //zarodnik poczatkowy
    pole[width / 2][height / 2] = 1;

    std::string plik0;
    std::ofstream f0;
    plik0 = "klastry-DLA-0.txt";
    f0.open(plik0);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            f0 << pole[j][i] << " ";
        }
        f0 << '\n';
    }
    f0.close( );

    //krok poruszania się
    int krokSet = 1;
    int krok;

    //komorki do usuniecia po iteracji
    std::vector<int> sasiedzi;

    //rozsiewamy czatki
    for (int i = 0; i < N; i++)
    {
        k.placement( );
        czastki.push_back( k );
    }

    std::cout << "test 2" << '\n';
    std::cout << czastki.size() << '\n';

    int counter_crush = 0;
    
    //póki czastki istnieja
    while (czastki.size( ))
    {
            

        for (int i = 0; i < czastki.size( ); i++)
        {
            //losujemy kierunek
            krok = rand( ) % 4;
            do { 
                //przemieszczamy
                if (krok == 0)
                {
                    //nie moze wyjsc poza tablice
                    if (czastki[i].x + 1 <= width)
                    {
                        czastki[i].x += krokSet;
                    }
                    else //odbicie od scianki tablicy
                    {
                        czastki[i].x -= krokSet;
                    }

                }
                else if (krok == 1)
                {
                    if (czastki[i].x - 1 >= 0)
                    {
                        czastki[i].x -= krokSet;
                    }
                    else
                    {
                        czastki[i].x += krokSet;
                    }
                }
                else if (krok == 2)
                {
                    if (czastki[i].y + 1 <= height)
                    {
                        czastki[i].y += krokSet;
                    }
                    else
                    {
                        czastki[i].y -= krokSet;
                    }
                }
                else if (krok == 3)
                {
                    if (czastki[i].y - 1 >= 0)
                    {
                        czastki[i].y -= krokSet;
                    }
                    else
                    {
                        czastki[i].y += krokSet;
                    }
                }
            }
            while (pole2[czastki[i].x][czastki[i].y]); //unikamy 2 czastek na sobie

            //przyklejenie
            //sasiedztwo z zarodnikiem
            if (
                (   //krawedzie
                    (czastki[i].x - 1 >= 0 && czastki[i].x + 1 <= width) &&
                    (czastki[i].y - 1 >= 0 && czastki[i].y + 1 <= height)
                ) &&
                (   //sasiedztwo
                    pole[czastki[i].x + 1][czastki[i].y] == 1 ||
                    pole[czastki[i].x - 1][czastki[i].y] == 1 ||
                    pole[czastki[i].x][czastki[i].y + 1] == 1 ||
                    pole[czastki[i].x][czastki[i].y - 1] == 1) &&
                //nie jest juz na zarosnietym
                pole[czastki[i].x][czastki[i].y] != 1)
            {
                std::cout << "crush! " << counter_crush << " " << czastki[i].x << " " << czastki[i].y << '\n';
                counter_crush++;

                pole[czastki[i].x][czastki[i].y] = 1;
                sasiedzi.push_back(i);
            }
        }

        //usuniecie przyklejonych z vektora
        for (int i = 0; i < sasiedzi.size( ); i++)
        {
            czastki.erase(czastki.begin( ) + (sasiedzi[i] - 1));
        }
        sasiedzi.clear( );
        //std::cout << czastki.size( ) << '\n';

    }

    std::cout << "test 3" << '\n';

    
    //pliki stuff
    std::string plik;
    std::ofstream f;
    plik = "klastry-DLA.txt";
    f.open(plik);

    int counter = 0;
    std::string tekst;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (pole[i][j] == 1)
            {
                tekst = "*";
            } else
            {
                tekst = " ";
            }
            
            
            f << tekst << " ";
            counter += pole[j][i];
        }
        f << '\n';
    }
    f.close( );

    std::cout << counter << " " << counter_crush << " " << N << '\n';

    std::cout << "test 4" << '\n';
}