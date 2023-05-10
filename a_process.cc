#include <iostream>

int main( int argc, char ** argv )
{
  std::string line;
  while ( std::cin >> line ) {
    std::cout << "You said: " << line << '\n';
  }
  return 1;
}
