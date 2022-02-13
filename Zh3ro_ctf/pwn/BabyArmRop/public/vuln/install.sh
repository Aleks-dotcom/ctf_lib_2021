pushd /tmp
wget -qO- ftp://ftp.gnu.org/gnu/gdb/gdb-8.2.tar.xz | tar Jxv
mkdir gdb
cd gdb
../gdb-8.2/configure  --enable-tui --with-expat --prefix=/usr/local  --target=arm-eabi --program-prefix=arm-eabi-
make all
sudo make  install
popd
