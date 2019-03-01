#include "func.h"

void insert(struct Tree_list *Tree, char *str)
{
    int end = 0;

    while(!end)
    {
        if(strcmp(str, Tree->Data.Word) > 0)
        {
            if(Tree->Right)
                Tree = Tree->Right;
            else
            {
                Tree->Right = malloc(sizeof(struct Tree_list));
                Tree = Tree->Right;
                Tree->Left = NULL;
                Tree->Right = NULL;
                Tree->Data.Count = 1;
                strcpy(Tree->Data.Word, str);
                end = 1;
            }
        }
        else
        {
            if(strcmp(str, Tree->Data.Word) < 0)
            {
                if(Tree->Left)
                    Tree = Tree->Left;
                else
                {
                    Tree->Left = malloc(sizeof(struct Tree_list));
                    Tree = Tree->Left;
                    Tree->Left = NULL;
                    Tree->Right = NULL;
                    Tree->Data.Count = 1;
                    strcpy(Tree->Data.Word, str);
                    end = 1;
                }
            }
            else
                if(strcmp(str, Tree->Data.Word) == 0)
                {
                    Tree->Data.Count++;
                    end = 1;
                }
        }
    }
}

void input_file(struct Tree_list *Tree, FILE *f)
{
    char *word_1;
    char word[MAX_WORD_SIZE];

    char str[MAX_STRING_SIZE];

    int end = 0;

    fgets(str, MAX_STRING_SIZE, f);

    if(Tree->Data.Count == 0)
    {
        //Tree = malloc(sizeof(struct Tree_list));
        word_1 = strtok(str, " ,.-:;");
        if(strchr(word_1, '\n'))
            word_1[strlen(word_1) - 1] = '\0';
        strcpy(word, word_1);
        strcpy(Tree->Data.Word, word);
        Tree->Data.Count = 1;
        Tree->Left = NULL;
        Tree->Right = NULL;
    }
    else
    {
        word_1 = strtok(str, " ,.-:;");
        if(strchr(word_1, '\n'))
            word_1[strlen(word_1) - 1] = '\0';
        strcpy(word, word_1);
        //printf("3 %s\n",word);
        if(*word)
            insert(Tree, word);
        //insert(Tree, word_1);
    }

    while(!end)
    {
        //printf("1 %s\n",word);
        word_1 = strtok(NULL, " ,.-:;");

        if(word_1)
        {
            if(strchr(word_1, '\n'))
            {
                word_1[strlen(word_1) - 1] = '\0';
            }
            //printf("2 %s\n",word);

            strcpy(word, word_1);
            //printf("3 %s\n",word);
            if(*word)
                insert(Tree, word);
            else
                end = 1;
        }
        else
            end = 1;
    }
    end = 0;

    while(fgets(str, MAX_STRING_SIZE, f))
    {
        word_1 = strtok(str, " ,.-:;");
        if(word_1)
        {
            if(strchr(word_1, '\n'))
                word_1[strlen(word_1) - 1] = '\0';

            strcpy(word, word_1);
            //printf("3 %s\n",word);
            if(*word)
                insert(Tree, word);
            else
                end = 1;
        }
        else
            end = 1;

        while(!end)
        {
            //printf("1 %s\n",word);
            word_1 = strtok(NULL, " ,.-:;");

            //printf("2 %s\n",word);
            if(word_1)
            {
                if(strchr(word_1, '\n'))
                    word_1[strlen(word_1) - 1] = '\0';
                strcpy(word, word_1);
                //printf("3 %s\n",word);
                if(*word)
                    insert(Tree, word);
                else
                    end = 1;
            }
            else
                end = 1;
        }
        end = 0;
    }

    rewind(f);
}

void output_tree(struct Tree_list *Tree, char *position, char *search)
{
    char NewPosition[100] = "\0";
    int index = 1;
    if(Tree != NULL)
    {
        strcpy(NewPosition, position);
        strcat(NewPosition, "R");
        output_tree(Tree->Right, NewPosition, search);

        if(strlen(position) > 0)
        {
            if(strlen(position) > 1)
            {
                while(position[index])
                {
                    if(position[index - 1] != position[index])
                    {
                        printf("%*c", (int)((MAX_WORD_SIZE + OFFSET_COUNT) * (1)), 179);

                    }
                    else
                    {
                        printf("%*c", (int)((MAX_WORD_SIZE + OFFSET_COUNT) * (1)), ' ');
                    }
                    index++;
                }

            }
        }
        if(strlen(position) > 0)
        {
            if(position[index - 1] == 'R')
            {
                printf("%*c", (int)((MAX_WORD_SIZE + OFFSET_COUNT) * (1)), 218);
            }
            else
            {
                printf("%*c", (int)((MAX_WORD_SIZE + OFFSET_COUNT) * (1)), 192);
            }

            for(int i = 0; i <  MAX_WORD_SIZE - strlen(Tree->Data.Word); i++)
                printf("%c", 196);
        }
        else
        {
            printf("%*c",(int)((MAX_WORD_SIZE - strlen(Tree->Data.Word))), ' ');
        }

        printf("%s%*d", Tree->Data.Word,OFFSET_COUNT, Tree->Data.Count);

        if(strcmp(Tree->Data.Word, search) == 0)
            printf(" <--------------------FIND--------------------\n");
        else
            printf("\n");


        NewPosition[0] = '\0';
        strcpy(NewPosition, position);
        strcat(NewPosition, "L");
        output_tree(Tree->Left, NewPosition, search);
    }
}

int search(struct Tree_list *Tree, char *search)
{
    while(Tree)
    {
        if(strcmp(Tree->Data.Word, search) == 0)
            return FIND;
        else
            if(strcmp(Tree->Data.Word, search) < 0)
                Tree = Tree->Right;
            else
                Tree = Tree->Left;

    }
    return NOT_FIND;
}

int search_in_file(FILE *f, char *search, int *first_input)
{
    rewind(f);
    int count = 0;
    int index = 0;
    *first_input = 0;
    char str[MAX_STRING_SIZE];
	//char c;

    while(fscanf(f, "%s", str) == 1)
    {
        index++;
        if(strcmp(str, search) == 0)
        {
			if(*first_input == 0)
				*first_input = index;
			count++;
        }
		//printf("%s \n", str);
    }
    return count; 
}

int delete_element(struct Tree_list *Tree, char *del)
{
    int delete_or_not = NOT_FIND;
    int end = 0;
    while(Tree && !end)
    {
        printf("1");
        if(strcmp((char*)Tree->Right->Data.Word, del) == 0)
        {
            printf("2");
            if(!Tree->Right->Left)
                Tree->Right = Tree->Right->Right;
            else
            {
                if(!Tree->Right->Right)
                    Tree->Right = Tree->Right->Left;
                else
                {
                    printf("2");
                    struct Tree_list *dop;
                    printf("2");
                    dop = Tree->Right;
                    printf("2");
                    while(dop->Right)
                        dop = dop->Right;
                    dop->Left = Tree->Left;

                    Tree->Right = Tree->Right->Right;
                }
            }
            end = 1;
        }
        else
            if(strcmp(Tree->Left->Data.Word, del) == 0)
            {
                if(!Tree->Left->Right)
                    Tree->Left = Tree->Left->Left;
                else
                    if(!Tree->Left->Left)
                        Tree->Left = Tree->Left->Right;
                    else
                    {
                        struct Tree_list *dop;

                        dop = Tree->Left;
                        while(dop->Left)
                            dop = dop->Left;
                        dop->Right = Tree->Right;

                        Tree->Left = Tree->Left->Left;
                    }
                end = 1;
            }
            else
            {
                if(strcmp(Tree->Data.Word, del) < 0)
                    Tree = Tree->Right;
                else
                    Tree = Tree->Left;
            }

    }
    if(!Tree)
        return delete_or_not;
    else
    {
        if(!Tree->Right)
        {
            Tree = Tree->Left;
        }
        else
        {
            if(!Tree->Right->Left)
                Tree->Right->Left = Tree->Left;
            else
            {
                struct Tree_list *dop = Tree;
                Tree = Tree->Right;

                while(Tree->Left)
                    Tree = Tree->Left;
                Tree->Left = dop->Left;

            }

        }
    }

    return FIND;
}

struct Tree_list *delete_tree(struct Tree_list *Tree, char *del)
{
    struct Tree_list *P, *v;

    if (!Tree)
          printf("warning: tree is empty\n");
    else if (strcmp(del, Tree->Data.Word) < 0)//x < Tree->inf)
      Tree->Left = delete_tree(Tree->Left, del);
    else if (strcmp(del, Tree->Data.Word) > 0)//x > Tree-> inf)
      Tree->Right = delete_tree(Tree->Right, del);
    else
    {
      P = Tree;
      if (!Tree->Right) Tree = Tree->Left;
      else if (!Tree->Left)
         Tree = Tree->Right;
      else
      {
         v = Tree->Left;
         if (v->Right)
         {
            while (v->Right->Right) v = v->Right;
            strcpy(Tree->Data.Word, v->Right->Data.Word);//Tree->inf = v->R->inf;
            Tree->Data.Count = v->Right->Data.Count;
            P = v->Right;
            v->Right = v->Right->Left;
         }
         else
         {
            Tree->Data.Count = v->Data.Count;
            strcpy(Tree->Data.Word, v->Data.Word);
            P = v;
            Tree->Left = Tree->Left->Left;
         }
      }
      free(P);
    }

    return Tree;

}

void func(struct Tree_list *root)
{	
	//printf("~~~~~\n");
    if (root->Left)
	{
        printf("%10s %d -- %10s %d [label=\"left\"];\n", root->Data.Word, root->Data.Count,
			(root->Left)->Data.Word, (root->Left)->Data.Count);
	}
	//printf("~\n");
    if (root->Right)
	{
        printf("%10s %d -- %10s %d [label=\"right\"];\n", root->Data.Word, root->Data.Count,
			(root->Right)->Data.Word, (root->Right)->Data.Count);
	}
	//printf("----\n");
}

void apply_post(struct Tree_list *root, void (*func)(struct Tree_list*))
{
	//printf("blok\n");
	if (root->Left)
	{
		apply_post(root->Left, func);
	}
	//printf("-ff\n");
	if (root->Right)
		apply_post(root->Right, func);
    func(root);
}

// обход дерева инфиксно
void apply_in(struct Tree_list *root, void (*func)(struct Tree_list*))
{
	if (root->Left)
		apply_in(root->Left, func);
    func(root);
	if (root->Right)
		apply_in(root->Right, func);
}

// обход дерева префиксно
void apply_pre(struct Tree_list *root, void (*func)(struct Tree_list*))
{
    func(root);
	if (root->Left)
		apply_pre(root->Left, func);
	if (root->Right)
		apply_pre(root->Right, func);
}
