# RAG Architecture 

LLM Limitations: Knowledge is constrained to what is included in training data.

RAG allows us to overcome this by integrating external data sources into LLM Applications.

RAG is a technique that enhances a model generation's by retrieving the relevant information from external sources. An external memory source can be an internal database, or the internet.
With RAG, only the information most relevant to the query is retrieved and input into the model.
Having access to relevant information can help the model generate more detailed responses while redcusing halucinations.

RAG Workflow/Architecture:
A RAG system has two components:
Retriever: retrieves information from extrenal memory sources
Generator: genrates response based on the retrieved information.

Preparing data for retrieval:

 1.Load : Load the documents to build the knowledge base

2. Split : Split them into chunks to be processed.

3. Embedding: Create numerical representations from text called embeddings

4. Store: These embeddings or vectors are stored in a vector database for future retrieval.

**Retrieval Algorithms:**

Retrieval works by ranking chunks based on their relevance to a given query.Retrieval algorithms differs based on how relevance scores are computed.

**Term-based retrieval: Uses TF-IDF algorithm** (Lexical leval)

When a user enters a query, the system searches for documents that share terms with the query.
Retrieved documents are ranked based on term frequency, document frequency, or more sophisticated measures like TF-IDF, BM25, or vector space models.

Example:
If a query is "machine learning":
The system finds all documents that contain the terms “machine” and “learning”.It ranks them based on how often those terms appear and how rare or significant they are.

**Embedding based retrieval:** (Semantic level)

Embedding based retrievers aim to rank documents/chunks based on how closely their meaning align with the query. This approach is also known as semantic retrieval.
1. converts the original data chunks into embeddings.
2. Stores the embeddings in a database called vector database.


# RAG_with_Langchain
**Load the documents using Langchain:**
CSV- CSVLoader: a dependency for loading csv files in LangChain, pdf- PyPdf: a dependency for loading PDF documents in LangChain, html- UnstructuredHTMLLoader: a dependency for loading html files in LangChain

**Splitting or Chunking**

Documents are splitted in chunks that contain sufficient context useful to LLM's.If the chunks are huge, retrieval will be slow and LLM may struggle to extract the most relevant context from the chunk to respond to query. 

chunk_size parameter is used to control this balance. Another parameter chunk_overlap is used to capture important information that may be lost around the boundaries between the chunk.

1. Charactertextsplitter: This method was also unable to create chunks that were all below the chunk_size by splitting by-paragraph.
2. Recursivecharactertextsplitter: We can improve with RecursiveCharacterTextSplitter.

**Embeddings and Storage**
Embeddings are numerical representations of text.
Embedding models aim to capture the "meaning" of the text, and these numbers map the text's position in a high-dimensional, or vector space.
When documents are embedded and stored, similar documents are located closer together in the vector space. When the RAG application receives a user input, it will be embedded and used to query the database, returning the most similar documents.


**LCEL Retrieval Chain**
Lang Chain Expression Language is a declarative syntax.
It is particularly relevant to RAG systems because it creates modular, reusable pipelines that can combine retrieval and generation components together.

**RAG Evaluation**
We can evaluate the retrieval process to check if the retrieved documents are relevant to the query, 
the generation process to see if the LLM hallucinated or misinterpreted the prompt, or 
the final output to measure the performance of the whole system.

Output accuracy: string evaluation
We can use LLMs to measure the correctness of the final output by comparing it to a reference answer. We'll assign the query, model's answer, and reference answer to compare with the following variables.
LangChainStringEvaluator from LangSmith, which is LangChain's platform for evaluating LLM applications. 

RAGAS Framework:
RAGAS was designed to evaluate both the retrieval and generation components of a RAG application.

Generation: Faithfulness, answer relevancy metrics from RAGAS

Retrieval: Context precision and context recall metrics from RAGAS

Faithfulness: Faithfulness assesses whether the generated output represents the retrieved documents well. It is calculated using LLMs to assess the ratio of faithful claims that can be derived from the context to the total number of claims. Because faithfulness is a proportion, it is normalized to between zero and one, where a higher score indicates greater faithfulness.

Context Precision: Context precision measures how relevant the retrieved documents are to the query. A context precision score closer to one means the retrieved context is highly relevant.

**RAG Graph:**

Vector RAG Limitations:
1.Document embedding captures semantic meaning but struggles to capture themes and relationships between entities in the document corpus.
2.As the volume of the database grows, the retrieval process can become less efficient, as the computational load increases with the search space.
3.Vector RAG systems don't easily accommodate structured or diverse data, which are harder to embed.
All of these challenges can be addressed by RAG Graphs.

Neo4j graph databases:
Neo4j is a powerful graph database option designed to store and efficiently query complex relationships.




**PineCone Database**

Pinecone is a vector database solution for building and scaling generative AI applications. 
It uses embeddings to store and retrieve data based on their semantic similarity, which is often integrated into chatbots, search engines, recommendation engines, or other AI systems. 

Indexes:
Indexes are one of the core components of the Pinecone infrastructure. 
They are used to store vectors and serve queries and other manipulations over the vectors it contains. 
Indexes contain records. Each vector is contained in a record, and the record also stores additional metadata that can be used in querying. 
It's also possible to create multiple indexes to house different datasets.

There are two types of indexes in Pinecone: 
Serverless and Pod-based indexes 
In pod-based indexes, we choose one or more pre-configured units of hardware, called pods, in which to create the index. Depending on the pod type chosen, we get different amounts of storage, query latency, and query throughput. 
Serverless indexes don't require managing resources; instead, they scale automatically depending on usage. 
Serverless indexes run as a managed service on a cloud platform, like AWS, and the vectors are stored in blob storage on that platform. In many cases, serverless indexes result in lower costs than pod-based indexes, which is leading many organizations to switch to serverless.



