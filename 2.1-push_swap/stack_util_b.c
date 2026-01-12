/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_util_b.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 17:01:53 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/12 17:02:01 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void ft_print_cost_lis(int **cost_lis, int size)
{
    int i;

    i = 0;
    while (i < size)
    {
        ft_printf("Cost LIS [%d]: %d\n", i, *cost_lis[i]);
        i++;
    }
}

void ft_debug_print_lis(char **lis, int size)
{
    int i;

    i = 0;
    ft_printf("LIS: ");
    while (i < size)
    {
        ft_printf("%d ", *lis[i]);
        i++;
    }
    ft_printf("\n");
}



int ft_calculate_lis(t_list *stack_a, int **arr, int **dp, int size)
{    
    int i = 0;
    int j = 0;
   
    t_list *curr = stack_a;
    int max_len = 0;



    return (max_len);
}

void    ft_set_max_lis(t_list *stack_a, int **dp, int max_index)
{
    int i;
    int start_value;

    i = 0;
    while (i < max_index)
    {
        if (dp[i] == max_index)
        {
            dp[i] = 1;
            start_value = *(int *)(stack_a)-> content; 
        }
        else if ( *(int *)(stack_a)-> content >= start_value)
            dp[i] = 1;
        else
            dp[i] = 0;
        i++;
    }
}

void ft_init_array_lis( int *lis, int size, int value)
{
    int i;

    i = 0;
    while (i < size)
    {
        lis[i] = value;
        i++;
    }
}

int	*ft_find_lis(t_list **stack_a, int size)
{
    int *lis_cost;
    int max_index;
    int *lis_mask;

    if (size == 0) return (0);

    lis_cost = malloc(sizeof(int) * size);
    lis_mask = malloc(sizeof(int) * size);
    if (!lis_cost || !lis_mask)
        return (NULL);

    ft_init_array_lis(lis_cost, size, 1);
    ft_init_array_lis(lis_mask, size, 0);
    max_index = ft_calculate_lis(*stack_a, &lis_cost, size);
    
    //ft_set_max_lis(*stack_a, &dp, max_index);
    free(lis_mask);


    
    

    return (lis_mask);

}

void    ft_push_non_lis(t_list **stack_a, t_list **stack_b, int *lis, int size)
{
    int i;

    i = 0;
    while (i < size)
    {
        if (lis[i] == 0)
        {
            ft_pa(stack_a, stack_b);
        }
        else
        {
            // Keep in stack_a
            ft_ra(stack_a);
        }
        i++;
    }
}