define github::clone($projectname, $base_url = "https://github.com", $build_dir = "/usr/src", $path = ['/usr/local/bin', '/usr/bin', '/bin']) {

	exec {"git clone $base_url/$projectname.git":
		require => Package['git'],
		cwd => $build_dir,
		path => $path,
		unless => "test -e $build_dir/$(basename $projectname)",
		timeout => 600,
	}
}
