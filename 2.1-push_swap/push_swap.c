/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 14:34:49 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 14:34:52 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int ft_is_str_digit(char *str)
{
    int i;

    i = 0;
    if (str[i] == '-' || str[i] == '+')
        i++;
    while (str[i])
    {
        if (ft_isdigit(str[i]) == 0)
            return (0);
        i++;
    }
    return (1);
}

void ft_list_print(t_list *lst)
{
    t_list *temp;

    temp = lst;
    while (temp)
    {
        ft_printf("%d\t", *(int *)temp->content);
        temp = temp->next;
    }
    ft_printf("\n");
}

int main(int argc, char **argv)
{
    int i;
    t_list *stack_a;
    t_list *stack_b;
    int num;
    void *content;

    stack_a = NULL;
    stack_b = NULL;

    i = 1;
    if (argc > 1){
        while (i < argc)
        {
            //ft_printf("Argv %s\n", argv[i]);
            if (ft_is_str_digit(argv[i]) == 0)
            {
                ft_printf("Error1\n");
                return (1);
            }
            else
            {
                num = ft_atoi(argv[i]);
                content = malloc(sizeof(int));
                *(int *)content = num;
                ft_lstadd_back(&stack_a, ft_lstnew(content));
            }
            i++;
        }
        #if DEBUG
        ft_printf("Stack A: "); ft_list_print(stack_a);
        ft_printf("Stack B: "); ft_list_print(stack_b);
        #endif
        ft_sort_stack(&stack_a, &stack_b);
        #if DEBUG
        ft_printf("After Sorting:\n");
        ft_printf("Stack A: "); ft_list_print(stack_a);
        ft_printf("Stack B: "); ft_list_print(stack_b);
        #endif
    }
    else
        ft_printf("Error\n");
    return (0);
}