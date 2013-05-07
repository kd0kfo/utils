import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.Path;
import java.net.URI;
import org.apache.hadoop.conf.Configuration;
import java.net.URISyntaxException;
import java.io.IOException;

public class copyMerge
{

    public static long fileSize(Path path, Configuration conf) throws IOException
    {
	long retval = 0;

	FileSystem fs = path.getFileSystem(conf);
	FileStatus stat = fs.getFileStatus(path);
	if(stat.isDir())
	    {
		FileStatus[] dirents = fs.listStatus(path);
		for(int i = 0;i<dirents.length;i++)
		    {
			retval += fileSize(dirents[i].getPath(),conf);
		    }
	    }
	else
	    {
		retval += stat.getLen();
	    }
		
	return retval;
    }

    public static void print_usage()
    {
	System.out.println("Usage: copyMerge <input directory> <output file name>");
    }

    public static void main(String[] args)
    {
	Configuration conf = new Configuration();
	
	if(args.length != 2)
	    {
		System.err.println("Invalid number of arguments.");
		System.out.println("");
		print_usage();
		System.exit(1);
	    }

	String indir = args[0];
	String outfile = args[1];
	Path inpath = new Path(indir);
	Path outpath = new Path(outfile);
	FileSystem infs,outfs;
	infs = outfs = null;
	String addString = null;

	try
	    {
		infs = FileSystem.get(new URI(indir), conf);
		outfs = FileSystem.get(new URI(outfile), conf);
	    }
	catch(URISyntaxException urise)
	    {
		System.err.println("Could not load URI: " + urise.getInput());
		System.err.println("Reason: " + urise.getReason());
		System.exit(1);
	    }
	catch(IOException ioe)
	    {
		System.err.println("Could not get FileSystem: " + ioe.getMessage());
		System.exit(1);
	    }
	
	System.out.println("Merging " + indir + " into " + outfile);
	
	try
	    {
		boolean copySuccess = FileUtil.copyMerge(infs, inpath, outfs, outpath, false, conf, addString);
		if(copySuccess)
		    System.out.println("Copy succeeded.");
		else
		    System.out.println("Copy failed.");
	    }
	catch(IOException ioe)
	    {
		System.err.println("File merge failed: " + ioe.getMessage());
                System.exit(1);
	    }


	try
	    {
		long inbytes = fileSize(inpath,conf);
		long outbytes = fileSize(outpath,conf);
		System.out.println("Read in " + Long.toString(inbytes) + " bytes");
		System.out.println("Merged " + Long.toString(outbytes) + " bytes");
		if(inbytes != outbytes)
		    {
			System.err.println("Input and output file sizes differ!");
			System.exit(1);
		    }
	    }
	catch(IOException ioe)
	    {
		System.err.println(ioe.getMessage());
		System.exit(42);
	    }
	

    }

}