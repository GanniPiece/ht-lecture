title:: 1958. Check if Move is Legal

- title:: 1958. Check if Move is Legal
	- class Solution {
	  public:
	    bool checkMove(vector<vector<char>>& board, int rMove, int cMove, char color) {
	        
	        for (int i = -1; i < 2; i++)
	        {
	            for (int j = -1; j < 2; j++)
	            {
	                if (i == 0 && j == 0)
	                    continue;
	                
	                // first around block
	                if (!isInBoard(rMove+i, cMove+j))
	                    continue;
	                
	                if (board[rMove+i][cMove+j] == '.' || 
	                    board[rMove+i][cMove+j] == color)
	                    continue;
	                
	                // (i, j) is the direction
	                int icheck = rMove + 2*i;
	                int jcheck = cMove + 2*j;
	                
	                while (isInBoard(icheck, jcheck))
	                {                    
	                    if (board[icheck][jcheck] == color)
	                    {
	                        return true;
	                    }
	                    else if (board[icheck][jcheck] == '.')
	                        break;
	                    // opposite color
	                    else
	                    {
	                        icheck += i;
	                        jcheck += j;
	                    }
	                    
	                }
	            }
	        }
	        
	        return false;
	    }
	    
	    bool isInBoard(int i, int j)
	    {
	        if (i < 0 || i >= 8)
	            return false;
	        else if (j < 0 || j >= 8)
	            return false;
	        
	        return true;
	    }
	  };
-