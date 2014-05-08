define github::install ($project, $base_dir = "/usr/src", $build_command = "python setup.py install", $onlyif = "test 1", $unless = "test 1 -eq 2", $path = ['/usr/local/bin', '/usr/bin', '/bin']) {

	exec {"install $project":
		command => $build_command,
		cwd => "$base_dir/$project",
		onlyif => $onlyif,
		unless => $unless,
		path => $path,
		timeout => 0,
	}
}
