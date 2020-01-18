<?php

/*
 *
 * MYTelkomsel VMP
 * @author Aruji, Irvan
 * @copyright TPP 2019 {author}
 * @description bacot ngentd.
 * @version V2 Consol
 * 
*/

echo "\033[01;31m
________             ________           ________    _______ 
___  __ \_______________  __/______________  /_ |  / /_|__ \
__  / / /  __ \_  ___/_  /  __  ___/  _ \_  /__ | / /____/ /
_  /_/ // /_/ /  /   _  /   _(__  )/  __/  / __ |/ / _  __/ 
/_____/ \____//_/    /_/    /____/ \___//_/  _____/  /____/                                                                                         
--------------- Team Pencari Proxy © 2019 -----------------
\n\033[0m";
function mintanomer(){
	print 'Masukin Nomor : ';
	$msisdn = trim(fgets(STDIN));
	return $msisdn;
}

function mintaotp(){
	print 'Masukkan otp : ';
	$otp = trim(fgets(STDIN));
	return $otp;
}

function beli(){
	echo "Masukkan ID Paket : ";
	$id = trim(fgets(STDIN));
	return $id;
}

function menu(){
	echo "
	=======================================
	1. Brute
	2. Manual ID
	3. Pilih Paket
	========================================
	\n";
	print 'Pilih : ';
	$pilihan = trim(fgets(STDIN));
	return $pilihan;
}

function reqotp($msisdn){
	$bahan = 'client_id=9yUwRUZirC0DXZyjMeQF4zCr6KO2R0Ub&connection=sms&phone_number=%2B';
	$body = "$bahan$msisdn";
	$header = array(
		'Accept: application/json', 
		'Content-Type: application/x-www-form-urlencoded; charset=utf-8',
		'Accept-Encoding: gzip, deflate, br', 'X-NewRelic-ID: VQ8GVFVVChAEUlJRBAcOUQ==',
		'content-length: 87',
		'User-Agent: okhttp/3.11.0'
	);

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://tdwidm.telkomsel.com/passwordless/start");
	curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie.txt');
	curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
	curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
	curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
	$hasil = curl_exec($ch);
}

function ip(){
	$ip = file_get_contents('https://api.ipify.org');
	echo "Ip Saat Ini : $ip\n";
}

function cekip($ip){
	
	$ch = curl_init();
	$header1 = array(
		'accept : application/json',
		"x-forwarded-for: $ip",
		'authorization: Bearer [object Object]',
		'transactionid: A901190719192442969383440',
		'channelid: VMP',
		'Connection: keep-alive',
		'Accept-Encoding: gzip',
		'User-Agent: okhttp/3.11.0',
		'X-NewRelic-ID: VQ8GVFVVChAEUlJRBAcOUQ==');
		
		curl_setopt($ch, CURLOPT_URL, 'https://vmp.telkomsel.com/api/sys/forwardIp');
		curl_setopt($ch, CURLOPT_HTTPHEADER, $header1);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie.txt');
		curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
		$hasil = curl_exec($ch);
}

function generate($msisdn,$otp){
	$l = 'client_id=9yUwRUZirC0DXZyjMeQF4zCr6KO2R0Ub&connection=sms&grant_type=password&username=%2B';
	$l1 = "$msisdn&password=$otp";
	$l2 = '&scope=openid%20offline_access&device=string';
	$login3 = "$l$l1$l2";

	$ch = curl_init();
	$header = array(
		'Accept: application/json', 
		'Content-Type: application/x-www-form-urlencoded; charset=utf-8',
		'Accept-Encoding: gzip, deflate, br', 'X-NewRelic-ID: VQ8GVFVVChAEUlJRBAcOUQ==',
		'content-length: 161',
		'User-Agent: okhttp/3.11.0'
	);
		curl_setopt($ch, CURLOPT_URL, 'https://tdwidm.telkomsel.com/oauth/ro');
		curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie.txt');
		curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
		curl_setopt($ch, CURLOPT_POSTFIELDS, $login3);
		$hasil = curl_exec($ch);
		$json_a = json_decode($hasil, true);
		if (strlen($json_a['id_token']) > 0) {
			$token = $json_a['id_token'];
			return $token;
		} else {
			echo "Jangan kelamaan masukin otp anjeng juga otp jangan salah";
		}
}

function login($token){
	$bod = "id_token=$token";
	$ch = curl_init();
	$header = array(
		'accept: application/json',
		'Content-Type: application/x-www-form-urlencoded; charset=utf-8',
		'Content-Length: 292',
		'Connection: Keep-Alive',
		'Accept-Encoding: gzip',
		'User-Agent: okhttp/3.11.0',
		'X-NewRelic-ID: VQ8GVFVVChAEUlJRBAcOUQ=='

	);
		curl_setopt($ch, CURLOPT_URL, 'https://tdwidm.telkomsel.com/tokeninfo');
		curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie.txt');
		curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
		curl_setopt($ch, CURLOPT_POSTFIELDS, $bod);
		$hasil = curl_exec($ch);
}

function mintapromote($msisdn,$token){
	$bod = '{"msisdn":"'.$msisdn.'"}';
	$ch = curl_init();
	$header = array(
		'accept: application/json',
		"authorization: Bearer $token",
		'transactionid: A901190719214506938000000',
		'channelid: VMP',
		'Content-Type: application/json;charset=utf-8',
		'Content-Length: 26',
		'Connection: Keep-Alive',
		'Accept-Encoding: gzip',
		'User-Agent: okhttp/3.11.0',
		'X-NewRelic-ID: VQ8GVFVVChAEUlJRBAcOUQ=='

	);
		curl_setopt($ch, CURLOPT_URL, 'https://vmp.telkomsel.com/api/user/');
		curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie.txt');
		curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PATCH");
		curl_setopt($ch, CURLOPT_POSTFIELDS, $bod);
		$hasil = curl_exec($ch);
		$json_a = json_decode($hasil, true);
		if (strlen($json_a['promotedToken']) > 0) {
			$promottoken = $json_a['promotedToken'];
			return $promottoken;
		} else {
			echo "Gadapet Token";
		}
}

function belipaket($id, $promottoken, $ccc){
	$bod = '{"toBeSubscribedTo":false}';
	$ch = curl_init();
	$header = array(
		'accept: application/json',
		"authorization: Bearer $promottoken",
		'transactionid: A901190719192442969383440',
		'channelid: VMP',
		'Content-Type: application/json;charset=utf-8',
		'Content-Length: 26',
		'Connection: Keep-Alive',
		'Accept-Encoding: gzip',
		'User-Agent: okhttp/3.11.0',
		'X-NewRelic-ID: VQ8GVFVVChAEUlJRBAcOUQ=='
	
	);
		curl_setopt($ch, CURLOPT_URL, "https://vmp.telkomsel.com/api/packages/$id");
		curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie.txt');
		curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");
		curl_setopt($ch, CURLOPT_POSTFIELDS, $bod);
		$hasil = curl_exec($ch);
		$json_a = json_decode($hasil, true);
		if($ccc == "y"){
			meseginfo($json_a,$id,"y",$promottoken);
		} else if($ccc == "n"){
			meseginfo($json_a,$id,"n",$promottoken);
		}
		
}

function meseginfo($json_a,$paketid,$zzz,$promottoken){
	if($zzz == "y"){
		if (strlen($json_a['message']) > 0)
		{
			$meseg = $json_a['message'];
			if ($meseg == "BIZ-UXP-0001") { echo "\n$paketid Paket tidak tersedia saat ini. Silakan coba beberapa saat lagi. (PRE-0001)"; }
			else if ($meseg == "BIZ-UXP-0002") { echo "\n$paketid Maaf,anda tidak memiliki cukup pulsa untuk membeli paket ini. Silakan isi ulang pulsa untuk melanjutkan. (PRE-0002)"; }
			else if ($meseg == "BIZ-UXP-0003") { echo "\n$paketid Kami tidak dapat menemukan paket yang cocok berdasarkan lokasi Anda saat ini. (PRE-0003)"; }
			else if ($meseg == "BIZ-UXP-0006") { echo "\n$paketid Paket tidak tersedia untuk hari ini. Silakan coba kembali. (PRE-0006)"; }
			else if ($meseg == "BIZ-UXP-0007") { echo "\n$paketid Paket tidak tersedia saat ini. Silakan coba kembali. (PRE-0007)"; }
			else if ($meseg == "BIZ-UXP-0008") { echo "\n$paketid Maaf, kuota paket ini sudah habis untuk hari ini. (PRE-0008)"; 
				$prin = fopen('hasil.txt', "w");
				fputs ("$prin", "$paketid"); }
			else if ($meseg == "BIZ-UXP-0009") { echo "\n$paketid Anda telah melebihi jumlah kuota Anda untuk dapat membeli paket ini. Silakan pilih paket lainnya. (PRE-0009)"; }
			else if ($meseg == "BIZ-UXP-0010") { echo "\n$paketid Nomor ponsel Anda tidak cocok dengan skema tarif untuk paket ini. Silakan pilih paket lainnya. (PRE-0010)"; }
			else if ($meseg == "BIZ-UXP-0011") { echo "\n$paketid Nomor ponsel Anda tidak memenuhi syarat untuk paket ini. Silakan pilih paket lainnya. (PRE-0011)"; }
			else if ($meseg == "BIZ-UXP-0013") { echo "\n$paketid Maaf,saat ini kami tidak dapat menemukan rincian info akun Anda. Silakan coba beberapa saat lagi. (PRE-0013)"; }
			else if ($meseg == "BIZ-UXP-0014") { echo "\n$paketid Maaf! Kami tidak dapat menemukan rincian dari akun Anda. Silakan coba beberapa saat lagi. (PRE-0014)"; }
			else if ($meseg == "BIZ-UXP-0015") { echo "\n$paketid Maaf, paket ini tidak tersedia untuk nomor ponsel Anda. Silakan pilih paket lainnya. (PRE-0015)"; }
			else if ($meseg == "BIZ-UXP-0016") { echo "\n$paketid Maaf, nomor ponsel Anda dalam masa tenggang. Silakan isi ulang pulsa untuk melanjutkan. (PRE-0016)"; }
			else if ($meseg == "BIZ-UXP-0017") { echo "\n$paketid Maaf, kuota untuk paket ini sudah habis. Silakan pilih paket lainnya. (PRE-0017)"; }
			else if ($meseg == "BIZ-UXP-1101") { echo "\n$paketid Transaksi Anda sebelumnya masih dalam proses. Silakan tunggu beberapa saat lagi.(PRE-1101)"; }
			else if ($meseg == "BIZ-UXP-1102") { echo "\n$paketid Maaf,saat ini paket tidak.....HILANG)"; }
			else { echo "\nID Paket tidak ditemukan"; }
		}
		else if ($json_a['notification'])
		{ 
			$ddd = $json_a['notification'];
			echo "\n$paketid $ddd";
			$prin = fopen('hasil.txt', "w");
			fputs ("$prin", "$paketid"); 
		}
	} else {
		if (strlen($json_a['message']) > 0)
		{
			$meseg = $json_a['message'];
			if ($meseg == "BIZ-UXP-0001") { echo "\n$paketid Paket tidak tersedia saat ini. Silakan coba beberapa saat lagi. (PRE-0001)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken); }
			else if ($meseg == "BIZ-UXP-0002") { echo "\n$paketid Maaf,anda tidak memiliki cukup pulsa untuk membeli paket ini. Silakan isi ulang pulsa untuk melanjutkan. (PRE-0002)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken); }
			else if ($meseg == "BIZ-UXP-0003") { echo "\n$paketid Kami tidak dapat menemukan paket yang cocok berdasarkan lokasi Anda saat ini. (PRE-0003)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken); }
			else if ($meseg == "BIZ-UXP-0006") { echo "\n$paketid Paket tidak tersedia untuk hari ini. Silakan coba kembali. (PRE-0006)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-0007") { echo "\n$paketid Paket tidak tersedia saat ini. Silakan coba kembali. (PRE-0007)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-0008") { echo "\n$paketid Maaf, kuota paket ini sudah habis untuk hari ini. (PRE-0008)"; 
				$prin = fopen('hasil.txt', "w");
				fputs ("$prin", "$paketid"); $dd = menu(); $zz = pilihanmenu($dd,$promottoken); }
			else if ($meseg == "BIZ-UXP-0009") { echo "\n$paketid Anda telah melebihi jumlah kuota Anda untuk dapat membeli paket ini. Silakan pilih paket lainnya. (PRE-0009)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-0010") { echo "\n$paketid Nomor ponsel Anda tidak cocok dengan skema tarif untuk paket ini. Silakan pilih paket lainnya. (PRE-0010)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-0011") { echo "\n$paketid Nomor ponsel Anda tidak memenuhi syarat untuk paket ini. Silakan pilih paket lainnya. (PRE-0011)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-0013") { echo "\n$paketid Maaf,saat ini kami tidak dapat menemukan rincian info akun Anda. Silakan coba beberapa saat lagi. (PRE-0013)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-0014") { echo "\n$paketid Maaf! Kami tidak dapat menemukan rincian dari akun Anda. Silakan coba beberapa saat lagi. (PRE-0014)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-0015") { echo "\n$paketid Maaf, paket ini tidak tersedia untuk nomor ponsel Anda. Silakan pilih paket lainnya. (PRE-0015)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-0016") { echo "\n$paketid Maaf, nomor ponsel Anda dalam masa tenggang. Silakan isi ulang pulsa untuk melanjutkan. (PRE-0016)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-0017") { echo "\n$paketid Maaf, kuota untuk paket ini sudah habis. Silakan pilih paket lainnya. (PRE-0017)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-1101") { echo "\n$paketid Transaksi Anda sebelumnya masih dalam proses. Silakan tunggu beberapa saat lagi.(PRE-1101)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else if ($meseg == "BIZ-UXP-1102") { echo "\n$paketid Maaf,saat ini paket tidak.....HILANG)"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
			else { echo "\nID Paket tidak ditemukan"; $dd = menu(); $zz = pilihanmenu($dd,$promottoken);}
		}
		else if ($json_a['notification'])
		{ 
			$ddd = $json_a['notification'];
			echo "\n$paketid $ddd";
			$prin = fopen('hasil.txt', "w");
			fputs ("$prin", "$paketid"); 
			$dd = menu();
			$zz = pilihanmenu($dd,$promottoken);
		}
	}
}

function brute($promottoken){
	echo 'Nilai Awal : ';
	$no1 = trim(fgets(STDIN));
	echo 'Nilai Akhir : ';
	$no2 = trim(fgets(STDIN));
	if(strlen($no1) == 4 && strlen($no2) == 4)
	{
		for($i = $no1; $i < $no2; ++$i) {
			$ass = "0000$i";
			belipaket($ass, $promottoken, "y");
		}
		$dd = menu();
		$zz = pilihanmenu($dd,$promottoken);
	}
	else if (strlen($no1) == 5 && strlen($no2) == 5)
	{
		for($i = $no1; $i < $no2; ++$i) {
			$ass = "000$i";
			belipaket($ass, $promottoken, "y");
		}
		$dd = menu();
		$zz = pilihanmenu($dd,$promottoken);
	}
	else{
		echo "Jangan sedikit jangan kebanyakan.";
		$dd = menu();
		$zz = pilihanmenu($dd,$promottoken);
	}

}

function pilihanmenu($pilihan,$promottoken){
	if ($pilihan == 1){
		brute($promottoken);
	}
	else if ($pilihan == 2){
		$a = beli();
		belipaket($a, $promottoken, "n");
		$dd = menu();
		$zz = pilihanmenu($dd,$promottoken);
	}
	else if ($pilihan == 3){
		echo "
		=======================================
		1. Maxstream 1GB 2hari Rp 10
		2. 5gb 30 hari Rp 10
		3. Combo Terbaik 15gb Rp 75rb
		4. 100MB_7Hari - MFS
		5. Maxtream 30gb 30k
		6. Promo 1GB 30 Hari 10k
		========================================
		\n";
		print 'Pilih : ';
		$pil = trim(fgets(STDIN));
		if ($pil == "1"){
			$id = "00009382";
			belipaket($id, $promottoken, "n");
		} else if ($pil == "2"){
			$id = "00017486";
			belipaket($id, $promottoken, "n");
		} else if ($pil == "3") {
			$id = "00013688";
			belipaket($id, $promottoken, "n");
		} else if ($pil == "4") {
			$id = "00009099";
			belipaket($id, $promottoken, "n");
		} else if ($pil == "5") {
			$id = "00007333";
			belipaket($id, $promottoken, "n");
		} else if ($pil == "6") {
			$id = "00007763";
			belipaket($id, $promottoken, "n");
		}
		else {echo "pilih bgsd :(";
			$dd = menu();
			$zz = pilihanmenu($dd,$promottoken);
		}
	}
	else {echo "pilih bgsd :(";
		$dd = menu();
		$zz = pilihanmenu($dd,$promottoken);
	} 
}

$a = mintanomer();
$b = reqotp($a);
$s = ip();
$s1 = cekip($s);
$c = mintaotp();
$d = generate($a, $c);
$e = login($d);
$f = mintapromote($a,$d);
$dd = menu();
$zz = pilihanmenu($dd,$f);

?>
