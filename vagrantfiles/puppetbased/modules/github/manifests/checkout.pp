define github::checkout ($project, $branch, $base_dir = "/usr/src", $path = ['/usr/local/bin', '/usr/bin', '/bin']) {
	exec {"git checkout $branch":
		cwd => "$base_dir/$project",
		path => $path,
	}
}
