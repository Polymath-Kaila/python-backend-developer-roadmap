## Streaming 
Its processing data in a continous flow of chunks so we can handle large or indefinite data sizes without ever loading it all into memory.  
Streaming matters:  
+ `scalability`: we can handle huge files.  
+ `Efficiency`:  we never need to hold the entire data in RAM.  
+ `Realtime streaming`: you can start working data as soon as the first chunk arrives.  

Its just processing chunks.  
Let’s say you have a large video file upload. You don’t read the whole video into memory. Instead, you read it in chunks and maybe write each chunk directly to cloud storage or.  process it as a stream. This way, you never overload your server’s memory.  

`memoryview` comes in when now we are dealing with large streams of data, where do not need to keep copying chuns around in memory.  
So we actually handle data without copying.  

Example all at work, buff, chunks, streaming + mv.  
```python
chunk_size = 8192
def stream_file(input_file, output_stream, chunk_size=8192):
    with open(input_file, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            mv = memoryview(chunk)
            # In a real scenario,we would stream this chunk to a network socket, cloud API, or another file
            output_stream.write(mv)

# Example usage: stream a large file to a new file
with open("output.dat", "wb") as out_f:
    stream_file("largefile.dat", out_f)
```