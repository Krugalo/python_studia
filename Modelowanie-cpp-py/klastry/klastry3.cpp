#include<iostream>
#include<random>
#include<cstdlib>
#include<fstream>
#include<time.h>
#include<vector>

class komorka
{
public:
    //parzystosc do hexagonalnosci
    bool p;
    //krysztal
    bool k = 0;
};

int main( )
{
    std::cout << "test 1" << '\n';

    //zmienne stale
    const int height = 100;
    const int width = 100;
    const int iteracje = 100;

    std::cout << "test 2" << '\n';
    
    //pole
    komorka k;
    std::vector<std::vector<komorka>> pole(height, std::vector<komorka>(width, k));
    std::vector<std::vector<komorka>> pole2(height, std::vector<komorka>(width, k));
    for (int j = 0; j < pole.size( ); j++)
    {
        for (int i = 0; i < pole[j].size(); i++)
        {
            pole[j][i].p = j%2;
        }
    }

    for (int j = 0; j < pole2.size( ); j++)
    {
        for (int i = 0; i < pole[j].size(); i++)
        {
            pole[j][i].p = j%2;
        }
    }

    //srodek pola
    pole[height / 2][width / 2].k = 1;
    pole2[height / 2][width / 2].k = 1;

    std::cout << "test 3 " << pole.size() << '\n';
    
    int sum = 0;
    for (int i = 0; i < iteracje; i++)
    {
        //lecimy po calym polu
        for (int j = 0; j < pole.size( ); j++)
        {
            //std::cout << j << '\n';

            for (int i = 0; i < pole[j].size( ); i++)
            {
                //std::cout << j << " " << i << '\n';

                //sprawdzamy sasiedztwo
                if (pole[i][j].p == 0)
                {
                    if (i - 1 >= 0 &&
                        i + 2 <= width &&
                        j - 1 >= 0 &&
                        j + 2 <= height)
                    {
                        sum =
                            pole[j][i - 1].k +
                            pole[j][i + 1].k +
                            pole[j - 1][i].k +
                            pole[j + 1][i].k +
                            pole[j + 1][i - 1].k +
                            pole[j - 1][i - 1].k;
                    }
                }
                else if (pole[i][j].p == 1)
                {
                    if (i - 1 >= 0 &&
                        i + 2 <= width &&
                        j - 1 >= 0 &&
                        j + 2 <= height)
                    {
                        sum =
                            pole[j][i - 1].k +
                            pole[j][i + 1].k +
                            pole[j - 1][i].k +
                            pole[j + 1][i].k +
                            pole[j + 1][i + 1].k +
                            pole[j - 1][i + 1].k;
                    }
                }

                //rozrastanie sie, warunek rozrastania
                if (sum == 1)
                {
                    pole2[j][i].k = 1;
                }
                sum = 0;
            }
        }

        //kopiujemy tempa na prawdziwa tablice
        for (int j = 0; j < pole.size( ); j++)
        {
            for (int i = 0; i < pole[j].size( ); i++)
            {
                pole[j][i].k = pole2[j][i].k;
            }
        }
    }

    std::cout << "test 4" << '\n';

    //plik
    //pliki stuff
    std::string plik;
    std::ofstream f;
    plik = "klastry-platek.txt";
    f.open(plik);

    std::string tekst;

    for (int i = 0; i < height; i++)
    {
        if (i%2 == 1)
            {
                f << " ";
            }
        for (int j = 0; j < width; j++)
        {
            if (pole[i][j].k == 1)
            {
                tekst = "*";
            } else
            {
                tekst = " ";
            }
            
            
            f << tekst << " ";
        }
        f << '\n';
    }
    f.close( );

    std::cout << "test 5" << '\n';
}