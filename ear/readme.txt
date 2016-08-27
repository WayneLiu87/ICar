耳朵：声音信号感知，翻译

计划：
 1: 语音识别:CMUSphinx, Juliusjs
 2: 命令训练:下载一些开源的中文语料库，初始几条控制命令
 3: 服务开发: 训练集管理，模型管理，服务开发

树莓派下Juliusjs安装：
step 1 : 升级gcc到4.8
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get dist-upgrade
  sudo rpi-update
  
  sudo apt-get install gcc-4.8 g++-4.8
 
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.6 20
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 50
  sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.6 20
  sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 50
  
step 2: nodejs安装
  cd somedir
  wget https://nodejs.org/dist/v4.5.0/node-v4.5.0.tar.gz
  tar -zxvf node-v4.5.0.tar.gz
  cd node-v4.5.0
  ./configure
  make(树莓派下这个步骤比较长，几个小时或10几个小时，注意不能断电）
  
step 3: 安装 Juliusjs
 bower install juliusjs --save
 
step 4: 测试
 git clone https://github.com/zzmp/juliusjs.git
 编辑测试程序：juliusjs/js/下的server.js, index.html
